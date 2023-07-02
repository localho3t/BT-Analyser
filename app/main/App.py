from termcolor import colored


class App:
    def __init__(self):
        self.start_msg()

    def start_msg(self):
        print(colored("[*] start application...", 'white'),
              colored("[Yes]", 'green'))
