from connection.create_DB import CreateDB
from termcolor import colored
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()


def check():
    try:
        host = os.getenv('DB_Host')
        user = os.getenv('DB_User')
        password = os.getenv('DB_Pass')

        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
        )

        print(colored('check connection ...',
              'yellow'), colored('[ok]', 'green'))
        CreateDB(mydb)
    except:
        print(colored('check connection ...',
              'yellow'), colored('[No]', 'red'))
        exit(0)
