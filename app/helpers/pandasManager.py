import pandas as pd
import numpy as np
import datetime
from helpers.fomatter import fmt

class PandasManager():
    def __init__(self) -> None:
        """This class handles most dataframes operations needed.

        """
        self.storage = {}

    """Formatter"""

    @fmt.format_dtypes
    def format_csv_from_binance(self, df_or_path):
        """Makes a OHLV dataframe from a csv downloaded from binance database

        Args:
            df_or_path (pd.DataFrame, str): can be the path to the csv file or a dataframe

        Returns:
            pd.Dataframe: Processed Dataframe
        """        
        if isinstance(df_or_path, str):
            df = pd.read_csv(df_or_path, index_col=False, header=None)
        df = df[list(range(0,6))]
        df.columns = ['open_time', 'open', 'high', 'low', 'close', 'volume']
        return df

    """Datetime management, to ensure every datetime object is UTC, all time mods
        must be done by these methods """

    def convert_df_times(self, df, target = "datetime", from_binance = True, custom_cols = False):
        """Method to convert date columns format

        Args:
            df (pd.Dataframe): dataframe to process
            target (str, optional): valid targets : "datetime", "timestamp". Defaults to "datetime".
            from_binance (bool, optional): If True, timestamps will be converted to utc datetimes. Defaults to True.
            custom_cols (bool, list, optional): list of specific cols to convert. Defaults to False.
        """
        
        target_cols = ["open_time", "start", "end", "date"]
        for col in target_cols:
            if col in df.columns:
                if target == 'datetime':
                    df[col] = [self.convert_timestamp_to_utc(x, from_binance=from_binance) for x in df[col]]
                elif target == 'timestamp' :
                    df[col] = [self.convert_utc_datetime_to_timestamp(x) for x in df[col]]
        return df
  
    def convert_timestamp_to_utc(self, timestamp, from_binance = True, unit="ms"):

        """used to correct errors when getting dates from database

        Returns:
            datetime.datetime: the utc datetime object
        """

        if from_binance:
            res = datetime.datetime.utcfromtimestamp(timestamp/1000)
        else:
            if unit == "ms":
                res = datetime.datetime.fromtimestamp(timestamp/1000)
            else : 
                res = datetime.datetime.fromtimestamp(timestamp)

        return res

    def convert_utc_datetime_to_timestamp(self, dt, units = "ms"):
        """Converts a datetime object to an int timestamp

        Args:
            dt (datetime): dt obj to convert
            units (str, optional): units. Defaults to "ms".

        Returns:
            int: timestamp
        """

        h = int(dt.replace(tzinfo = datetime.timezone.utc).timestamp())
        if units == "ms":
            h = int(h*1000)
        return h



pdm = PandasManager()