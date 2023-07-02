from connection.create_DB import CreateDB
from connection.querys import Querys
from termcolor import colored
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()


class Connection:
    host = os.getenv('DB_Host')
    user = os.getenv('DB_User')
    password = os.getenv('DB_Pass')
    database = os.getenv('DB_Name')
    querys = Querys()
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    mycursor = mydb.cursor()
