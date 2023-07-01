from termcolor import colored
from dotenv import load_dotenv
import os
load_dotenv()


def exists_os():
    flag = 1
    if os.getenv('File_PATH') == "":
        print(colored("File_PATH is check ...", 'yellow'),
              colored('[No]', 'red'))
        flag = 0
    else:
        print(colored("DB_Name is check ...", 'yellow'),
              colored('[ok]', 'green'))

    #
    if os.getenv('DB_Name') == "":
        print(colored("DB_Name is check ...", 'yellow'),
              colored('[No]', 'red'))
    else:
        print(colored("DB_Name is check ...", 'yellow'),
              colored('[ok]', 'green'))
    #
    if os.getenv('DB_User') == "":
        print(colored("DB_User is check ...", 'yellow'),
              colored('[No]', 'red'))
    else:
        print(colored("DB_User is check ...", 'yellow'),
              colored('[ok]', 'green'))
    #
    if os.getenv('DB_Pass') == "":
        print(colored("DB_Pass is check ...", 'yellow'),
              colored('[No]', 'red'))
    else:
        print(colored("DB_Pass is check ...", 'yellow'),
              colored('[ok]', 'green'))
    #
    if os.getenv('DB_Host') == "":
        print(colored("DB_Host is check ...", 'yellow'),
              colored('[No]', 'red'))
    else:
        print(colored("DB_Host is check ...", 'yellow'),
              colored('[ok]', 'green'))
    #
    if os.getenv('Delay') == "":
        print(colored("Delay is check ...", 'yellow'),
              colored('[No]', 'red'))
    else:
        print(colored("Delay is check ...", 'yellow'),
              colored('[ok]', 'green'))
    #
    if flag == 0:
        print(colored("[!] Error File Path ... ", 'red'))
        exit(0)
