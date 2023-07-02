from termcolor import colored
from app.fileReader.logReader import LogReader


class App:
    def __init__(self):
        self.start_msg()

    def start_msg(self):
        print(colored("[*] start application...", 'white'),
              colored("[Yes]", 'green'))
        self.start()

    def start(self):
        LogReader()
