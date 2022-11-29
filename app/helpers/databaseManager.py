import os
import sqlite3
from helpers.fomatter import fmt
import pandas as pd



class DataBaseManager():

    def __init__(self, path_to_database, allow_new = True):
        
        """This class will perform all the work on the Database,
        It should be the only instance to acces the DB.

        If allow_new is True, if the path provided is no file,
        A new db will be created at the indicated path
        
        """


        self.path_to_db = self.check_path(path_to_database, allow_new)
        self.con = self.get_con()

    def __str__(self) -> str:
        return "Database Manager"        



    #init functions

    def check_path(self, path, allow_new):
        

        if path[-2:] != 'db':
            raise NameError('Input path is not a .db extension')

        if os.path.isdir("/".join(path.split("/")[:-1])):
            return path
        else:
            if allow_new:
                os.makedirs("/".join(path.split("/")[:-1]))
                return path
            else:
                raise FileNotFoundError("Database not found, check the input path")

    def get_con(self):
        """Connects to the database and return the con object
        """
        return sqlite3.connect(self.path_to_db)
            
    def write_table(self, df, table_name, if_exists='replace'):
        """method to add or append to a table on the database

        Args:
            df (pd.DataFrame): the dataframe to process
            table_name (str): the name of the db table
            if_exists (str, optional): valid choices ['replace', 'append']. How to behave when table exists already. Defaults to 'replace'.
        """

        type_serie = pd.Series({k:v for k, v in fmt.df_types.items() if k in df.columns})
        

        
        


        