import mysql.connector
import os
from dotenv import load_dotenv
from termcolor import colored


def log_create():
    try:
        print(colored('create log table ...',
                      'yellow'), colored('[wait]', 'yellow'))
        host = os.getenv('DB_Host')
        user = os.getenv('DB_User')
        password = os.getenv('DB_Pass')
        database = os.getenv('DB_Name')

        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        mycursor = mydb.cursor()
        mycursor.execute(
            "CREATE TABLE `log` (`id` int(11) NOT NULL,\
                `response` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK(json_valid(`response`)),\
                `headers` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK(json_valid(`headers`)),\
                `request_count` int(11) NOT NULL,\
                `created_at` timestamp NOT NULL ,\
                `update_at` datetime NOT NULL,\
                `avrg_volume` double NOT NULL\
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci\
            ")
        print(colored('[*] log table in bt_Analyser was created!',
                      'green'))
    except:
        try:
            host = os.getenv('DB_Host')
            user = os.getenv('DB_User')
            password = os.getenv('DB_Pass')
            database = os.getenv('DB_Name')
            mydb = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM log")
            print(colored('[*] There are log table in bt_Analyser databases',
                          'green'))
        except:

            print(colored("[!] Error DB running ", 'red'))
