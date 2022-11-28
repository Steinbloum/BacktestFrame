from helpers.databaseManager import DataBaseManager
from helpers.inouts import Inout
import os
import shutil
import pytest


io = Inout()

@io.test_wrap
def test_database_path_input():
    
    good_path = "app/tests/sample_data/test_db/test_db.db"
    bad_name = "app/tests/sample_data/test_db/test_db.csv"
    bad_path = "app/tests/sample_data/test_db/bad_path/test_db.db"

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








