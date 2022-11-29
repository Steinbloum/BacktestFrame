import numpy as np


class Formatter:
    def __init__(self) -> None:

        """This class is used to ensure the data is of the right type/format
        """


        self.df_types = dict(
            open = np.float64,
            high = np.float64,
            low = np.float64,
            close = np.float64,
            volume = np.float64,
            ticker = str,
            asset = str,
            quote = str,
            tf = str,
            span = np.int64,
            )

    def format_dtypes(self,func):
        """Decorator used to format a dataframe to the types in self.types

        Args:
            func (function): function returning a dataframe
        """
        def wrapper(*args, **kwargs):

            res = func(*args, **kwargs)
            return res.astype({k : v for k, v in self.df_types.items() if k in res.keys()})

        return wrapper





fmt = Formatter()