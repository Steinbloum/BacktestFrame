from helpers.pandasManager import pdm
from helpers.inouts import Inout
import numpy as np



io = Inout()

@io.test_wrap
def test_format_csv_from_binance():
    
    df = pdm.format_csv_from_binance("app/tests/sample_data/BCHUSDT-1m-2022-09.csv")
    assert df["open_time"].dtype == np.int64
    assert df["open"].dtype == np.float64
    assert df["high"].dtype == np.float64
    assert df["low"].dtype == np.float64
    assert df["close"].dtype == np.float64

@io.test_wrap
def test_convert_timestamps_to_utc_datetime():
    df = pdm.format_csv_from_binance("app/tests/sample_data/BCHUSDT-1m-2022-09.csv")
    df = pdm.convert_df_times(df)
    assert df.open_time.iloc[0].hour == 0
    assert df.open_time.iloc[0].minute == 0

@io.test_wrap
def test_convert_utc_datetime_to_timestamp():
    df = pdm.format_csv_from_binance("app/tests/sample_data/BCHUSDT-1m-2022-09.csv")
    dfb = pdm.convert_df_times(df)
    dfb = pdm.convert_df_times(df, "timestamp")
    assert df.equals(dfb)








