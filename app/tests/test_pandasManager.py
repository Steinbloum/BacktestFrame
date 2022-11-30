from helpers.pandasManager import pdm
from helpers.inouts import Inout
import numpy as np
import pytest
import pandas as pd
from helpers.fomatter import fmt



io = Inout()

@io.test_wrap
def test_format_csv_from_binance():
    
    df = pdm.format_csv_from_binance("app/tests/sample_data/BCHUSDT-1m-2022-09.csv")
    dtype_target = fmt.make_dtype_serie(df).to_dict()
    for col in df.columns:
        if col in dtype_target.keys():
            assert dtype_target[col] == df.dtypes[col]

    

@io.test_wrap
def test_convert_timestamps_to_utc_datetime():
    df = pdm.format_csv_from_binance("app/tests/sample_data/BCHUSDT-1m-2022-09.csv")
    df = pdm.convert_df_times(df)
    assert df.open_time.iloc[0].hour == 0
    assert df.open_time.iloc[0].minute == 0

    df2 = pdm.convert_df_times(df)
    assert df.equals(df2)


@io.test_wrap
def test_convert_utc_datetime_to_timestamp():
    df = pdm.format_csv_from_binance("app/tests/sample_data/BCHUSDT-1m-2022-09.csv")
    dfb = pdm.convert_df_times(df)

    dfb = pdm.convert_df_times(df, "timestamp")
    assert df.equals(dfb)

    dfb2 = pdm.convert_df_times(df, "timestamp")
    assert dfb2.equals(dfb)






