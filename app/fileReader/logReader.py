import os
from dotenv import load_dotenv
from termcolor import colored
from app.spliter.spliter_app import SpliterApp
from app.kernel.Kernel import Kernel
load_dotenv()


def LogReader():
    sa = SpliterApp()
    kernel = Kernel()
    data_log = []
    print(colored("[*] Running program ...", 'green'))

    try:
        f = open(os.getenv('File_PATH'), 'r')
        lines = f.readlines()
        for i in lines:
            sa.setData(i)
            data = sa.getInformation()
            data_log.append(data)
        kernel.analyze(data_log)
    except FileNotFoundError:
        print(colored("[!] Not Found File . pls edit .env", 'red'))
        exit(0)


def main():

    LogReader()
