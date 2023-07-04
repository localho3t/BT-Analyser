from termcolor import colored
from app.fileReader.logReader import main
import datetime
from time import sleep
import os
from app.banner.v1.banner import banner
from dotenv import load_dotenv
load_dotenv()

class App:
    def __init__(self):
        self.start_msg()

    def start_msg(self):
        print(colored("[*] start application...", 'white'),
              colored("[Yes]", 'green'))
        self.start()

    def start(self):
        os.system("clear")
        banner()
        print(
            colored(
                f"[{str(datetime.datetime.now()).split('.')[0]}]", "red"),
            colored("app start ...", "green"),
        )
        while True:
            try:

                main()
                print(
                    colored(
                        f"[{str(datetime.datetime.now()).split('.')[0]}]", "red"),
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
