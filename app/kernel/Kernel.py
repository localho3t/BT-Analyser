from dotenv import load_dotenv
from termcolor import colored
from connection.controller.logController import logController
from connection.controller.traficController import traficController
from app.kernel.analyse.kernel_analyse import KernelAnalyser


load_dotenv()


class Kernel:
    Kernel_Analyse = KernelAnalyser()
    logController = logController()
    traficController = traficController()

    def analyze(self, data):
        information = self.Kernel_Analyse.setDate(data)
        self.traficController.select_insert(information[1])
        self.logController.select_insert(information[0])

