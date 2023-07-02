from time import sleep
import mysql.connector
from termcolor import colored
from connection.table.log_table import log_create
import os
from dotenv import load_dotenv
load_dotenv()


def DBNameCheck():
    if not "DB_Name" in os.environ:
        f = open('.env', 'a+')
        f.write("DB_Name=\"bt_Analyser\"\n")
        f.close()
        load_dotenv()


def CreateDB(data):
    sleep(3)
    print(colored('create database ...',
                  'yellow'), colored('[wait]', 'yellow'))
    mycursor = data.cursor()
    DBNameCheck()
    #
    try:
        mycursor = data.cursor()

        mycursor.execute("CREATE DATABASE bt_Analyser")
        print(colored('[*] Database bt_Analyser was created!',
                      'green'))
        log_create()
    except:
        try:
            mycursor.execute("use bt_Analyser")
            print(colored('[*] There are bt_Analyser databases',
                          'green'))
            log_create()

        except:
            print(colored('CREATE DATABASE ...',
                          'yellow'), colored('[No]', 'red'))
            print(colored("[!] Error DB informations ... ", 'red'))
            exit(0)
