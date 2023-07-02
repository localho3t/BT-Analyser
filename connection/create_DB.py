import mysql.connector
from termcolor import colored
from connection.table.log_table import log_create


def CreateDB(data):
    print(colored('create database ...',
                  'yellow'), colored('[wait]', 'yellow'))
    try:
        mycursor = data.cursor()
        mycursor.execute("CREATE DATABASE bt_Analyser")
        f = open('.env', 'a+')
        f.write("DB_Name=\"bt_Analyser\"\n")
        print(colored('[*] Database bt_Analyser was created!',
              'green'))
        log_create()
    except:
        print(colored('CREATE DATABASE ...',
              'yellow'), colored('[No]', 'red'))
        print(colored("[!] Error DB informations ... ", 'red'))
        exit(0)
