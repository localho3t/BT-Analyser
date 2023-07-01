import os
from termcolor import colored


def env_check():
    from app.envChecker.exists_os import exists_os
    if os.path.exists(".env"):
        print(colored(".env is check ...", 'yellow'), colored('[ok]', 'green'))
        flag = exists_os()
    else:
        from app.envChecker.create_env import create
        print(colored(".env is check ...", 'yellow'), colored('[No]', 'red'))
        print(colored("wite...", 'yellow'), colored('[3s]', 'red'))
        print(colored(".env is complate", 'yellow'), colored('[ok]', 'green'))

        create()
