import datetime
from time import sleep
import os
from dotenv import load_dotenv
from termcolor import colored
from connection.controller.logController import logController
from connection.controller.traficController import traficController
from app.kernel.analyse.kernel_analyse import KernelAnalyser
from app.banner.v1.banner import banner


load_dotenv()


class Kernel:
    Kernel_Analyse = KernelAnalyser()
    logController = logController()
    traficController = traficController()

    def analyze(self, data):
        os.system("clear")
        banner()
        print(
            colored(f"[{str(datetime.datetime.now()).split('.')[0]}]", "red"),
            colored("app start ...", "green"),
        )
        while True:
            try:
                information = self.Kernel_Analyse.setDate(data)
                self.traficController.select_insert(information[1])
                self.logController.select_insert(information[0])
                print(
                    colored(f"[{str(datetime.datetime.now()).split('.')[0]}]", "red"),
                    colored("i am still alive ...", "green"),
                )
                sleep(int(os.getenv("Delay")))
            except KeyboardInterrupt:
                print("by :)")
                exit(0)
            except ConnectionRefusedError:
                print(
                    colored(
                        f"[{str(datetime.datetime.now()).split('.')[0]}]", "yellow"
                    ),
                    colored("I died", "red"),
                )
