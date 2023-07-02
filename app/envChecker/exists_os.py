from termcolor import colored
from dotenv import load_dotenv
import os
load_dotenv()


def print_functions(msg, msg2, color):
    print(colored(f"{msg} is check ...", 'yellow'),
          colored(f"[{msg2}]", f"{color}"))


def exists_os():
    flag = 1
    cp = 0
    # ====================================================
    if os.getenv('File_PATH') == "":
        print_functions('File_PATH', 'No', 'red')
        flag = 0
    else:
        print_functions('File_PATH', 'ok', 'green')
    #
    if os.getenv('DB_User') == "":
        flag = 2
        print_functions('DB_User', 'No', 'red')
    else:
        cp += 1
        print_functions('DB_User', 'ok', 'green')
    #
    if os.getenv('DB_Pass') == "":
        # flag = 2
        print_functions('DB_Pass', 'No', 'red')
    else:
        # cp += 1
        print_functions('DB_Pass', 'ok', 'green')
    #
    if os.getenv('DB_Host') == "":
        flag = 2
        print_functions('DB_Host', 'No', 'red')
    else:
        cp += 1
        print_functions('DB_Host', 'ok', 'green')
    #
    if os.getenv('Delay') == "":
        flag = 3
        print_functions('Delay', 'No', 'red')
    else:
        print_functions('Delay', 'ok', 'green')
    # ====================================================
    if flag == 0:
        print(colored("[*] start application...", 'white'),
              colored("[No]", 'red'))
        print(colored("[!] Error File Path ... ", 'red'))
        exit(0)
    elif flag == 2:
        print(colored("[*] start application...", 'white'),
              colored("[No]", 'red'))
        print(colored("[!] Error DB informations ... ", 'red'))
        exit(0)
    elif flag == 3:
        print(colored("[*] start application...", 'white'),
              colored("[No]", 'red'))
        print(colored("[!] Error Delay value ... ", 'red'))
        exit(0)
    else:
        print(colored("[*] start application...", 'white'),
              colored("[Yes]", 'green'))
    if cp == 2:
        from connection.checkConnection import check
        check()
