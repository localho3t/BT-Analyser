from termcolor import colored
from dotenv import load_dotenv
import os
load_dotenv()


def print_functions(msg, msg2, color):
    print(colored(f"{msg} is check ...", 'yellow'),
          colored(f"[{msg2}]", f"{color}"))


def exists_os():
    flag = 1
    # ====================================================
    if os.getenv('File_PATH') == "":
        print_functions('File_PATH', 'No', 'red')
        flag = 0
    else:
        print_functions('File_PATH', 'ok', 'green')
    #
    if os.getenv('DB_Name') == "":
        print_functions('DB_Name', 'No', 'red')
    else:
        print_functions('DB_Name', 'ok', 'green')
    #
    if os.getenv('DB_User') == "":
        print_functions('DB_User', 'No', 'red')
    else:
        print_functions('DB_User', 'ok', 'green')
    #
    if os.getenv('DB_Pass') == "":
        print_functions('DB_Pass', 'No', 'red')
    else:
        print_functions('DB_Pass', 'ok', 'green')
    #
    if os.getenv('DB_Host') == "":
        print_functions('DB_Host', 'No', 'red')
    else:
        print_functions('DB_Host', 'ok', 'green')
    #
    if os.getenv('Delay') == "":
        print_functions('Delay', 'No', 'red')
    else:
        print_functions('Delay', 'ok', 'green')
    # ====================================================
    if flag == 0:
        print(colored("[*] start application...", 'white'),
              colored("[No]", 'red'))
        print(colored("[!] Error File Path ... ", 'red'))
        exit(0)
    else:
        print(colored("[*] start application...", 'white'),
              colored("[Yes]", 'green'))
