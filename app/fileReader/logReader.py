import os
from dotenv import load_dotenv
from termcolor import colored
from app.spliter.spliter_app import SpliterApp
load_dotenv()


def LogReader():
    sa = SpliterApp()
    try:
        f = open(os.getenv('File_PATH'), 'r')
        lines = f.readlines()
        for i in lines:
            sa.setData(i)
            data = sa.getInformation()
            print(data)
            break
    except FileNotFoundError:
        print(colored("[!] Not Found File . pls edit .env", 'red'))
        exit(0)
