from termcolor import colored
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()


def check():
    try:
        user = os.getenv('DB_User')
        password = os.getenv('DB_Pass')
        host = os.getenv('DB_Host')

        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
        )
        print(colored('check connection ...',
              'yellow'), colored('[ok]', 'green'))
    except:
        print(colored('check connection ...',
              'yellow'), colored('[No]', 'red'))
        print(colored("[!] Error DB informations ... ", 'red'))
        exit(0)
