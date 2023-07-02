import datetime
from time import sleep
import os
from dotenv import load_dotenv
from termcolor import colored
from connection.controller.logController import logController
from app.kernel.analyse.kernel_analyse import KernelAnalyser
load_dotenv()


class Kernel:
    Kernel_Analyse = KernelAnalyser()
    logController = logController()

    def analyze(self, data):
        os.system('clear')
        print(colored(f"[{datetime.datetime.now()}]", 'red'),
              colored('app start ...', 'green'))
        while True:
            try:
                information = self.Kernel_Analyse.setDate(data)
                self.logController.select_insert(information)
                print(colored(f"[{datetime.datetime.now()}]", 'red'),
                      colored('i am still alive ...', 'green'))
                sleep(int(os.getenv('Delay')))
            except KeyboardInterrupt:
                print("by :)")
                exit(0)
            except ConnectionRefusedError:
                print(colored(f"[{datetime.datetime.now()}]", 'yellow'),
                      colored('I died', 'red'))
