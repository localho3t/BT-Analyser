import mysql.connector
import os
from dotenv import load_dotenv
from termcolor import colored


def trafic_report_create():
    try:
        print(
            colored("create trafic_report table ...", "yellow"),
            colored("[wait]", "yellow"),
        )
        host = os.getenv("DB_Host")
        user = os.getenv("DB_User")
        password = os.getenv("DB_Pass")
        database = os.getenv("DB_Name")

        mydb = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )
        mycursor = mydb.cursor()
        mycursor.execute(
            "CREATE TABLE `trafic_report` (\
            `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,\
            `data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`data`)),\
            `date` date UNIQUE KEY NOT NULL\
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;"
        )

        print(colored("[*] trafic_report table in bt_Analyser was created!", "green"))
    except:
        try:
            host = os.getenv("DB_Host")
            user = os.getenv("DB_User")
            password = os.getenv("DB_Pass")
            database = os.getenv("DB_Name")
            mydb = mysql.connector.connect(
                host=host, user=user, password=password, database=database
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM log")
            print(
                colored(
                    "[*] There are trafic_report table table in bt_Analyser databases",
                    "green",
                )
            )
        except:
            print(colored("[!] Error DB running ", "red"))
