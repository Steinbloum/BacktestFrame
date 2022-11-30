from helpers.databaseManager import DataBaseManager
from helpers.pandasManager import pdm
from helpers.inouts import Inout
import os
import shutil
import pytest
import pandas as pd

io = Inout()

test_path = "app/tests/db/db_test.db"


def clear_table(func):
    """deletes database before and after the test func

    Args:
        func (_type_): _description_
    """
    def wrapper(*args, **kwargs):
        try:
            shutil.rmtree("/".join(test_path.split("/")[:-1]))
        except FileNotFoundError:
            pass
        func(*args, **kwargs)
        try:
            shutil.rmtree("/".join(test_path.split("/")[:-1]))
        except FileNotFoundError:
            pass
    return wrapper

@clear_table
@io.test_wrap
def test_database_path_input():
    
    good_path = test_path
    bad_name = test_path+"f"
    bad_path = "app/tests/db/bad_path/db_test.db"

    #test good path
    dbm = DataBaseManager(good_path)
    assert os.path.isfile(good_path)
    shutil.rmtree("/".join(good_path.split("/")[:-1])+"/")

    #test bad_path_allow_new : 
    dbm = DataBaseManager(bad_path)
    assert os.path.isfile(bad_path)
    shutil.rmtree("/".join(good_path.split("/")[:-1])+"/")

    #test bad_path_allow_new = False:
    with pytest.raises(FileNotFoundError, match="Database not found, check the input path"):
        dbm = DataBaseManager(bad_path, allow_new=False)
    
    #test bad name
    with pytest.raises(NameError, match = "Input path is not a .db extension"):
        dbm = DataBaseManager(bad_name)

@io.test_wrap
def test_write_table():
    dbm = DataBaseManager(test_path)
    df = pdm.format_csv_from_binance("app/tests/sample_data/BCHUSDT-1m-2022-09.csv")
    dbm.write_table(df, 'test_table')
    assert len(dbm.get_tables_list()) == 1
    assert dbm.get_tables_list()[0] == "test_table"
    assert dbm.get_table_lenght('test_table')["count(*)"].iloc[0] == len(df)

@io.test_wrap
def test_get_whole_df():
    dbm = DataBaseManager(test_path)
    df = dbm.get_whole_df("test_table")
    assert df.equals(pdm.format_csv_from_binance("app/tests/sample_data/BCHUSDT-1m-2022-09.csv"))

@clear_table
def test_delete_test_db():
    pass


    







