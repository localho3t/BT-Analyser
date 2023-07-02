from time import sleep
import os
from dotenv import load_dotenv
from app.kernel.analyse.kernel_analyse import KernelAnalyser
load_dotenv()


class Kernel:
    Kernel_Analyse = KernelAnalyser()

    def analyze(self, data):
        try:
            self.Kernel_Analyse.setDate(data)
            sleep(int(os.getenv('Delay')))
        except KeyboardInterrupt:
            print("by :)")
            exit(0)
