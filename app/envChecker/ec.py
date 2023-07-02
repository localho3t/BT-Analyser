import os
from termcolor import colored


def env_check():
    from app.envChecker.exists_os import exists_os
    if os.path.exists(".env"):
        print(colored(".env is check ...", 'yellow'), colored('[ok]', 'green'))
        exists_os()
    else:
        try:
            from app.envChecker.create_env import create
            print(colored(".env is check ...", 'yellow'),
                  colored('[No]', 'red'))
            print(colored("wait...", 'yellow'), colored('[3s]', 'red'))
            print(colored(".env is complate", 'yellow'),
                  colored('[ok]', 'green'))
            File_PATH = input("Enter log File Path >> ")
            DB_Host = input("Enter DB HOST >> ")
            DB_User = input("Enter DB User >> ")
            DB_Pass = input("Enter DB Pass >> ")
            Delay = input("Enter Delay >> [d:30]")
            if Delay == "":
                Delay = 30
            if File_PATH == "":
                print(
                    colored("file path and DB Host and User And Password is required", 'red'))
                exit(0)
            create(DB_Host, DB_User, DB_Pass, int(Delay), File_PATH)
            exists_os()
        except KeyboardInterrupt:
            print(
                colored("file path and DB Host and User And Password is required", 'red'))
