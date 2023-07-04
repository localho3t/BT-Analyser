import matplotlib.pyplot as plt
import datetime

class ReportGenerate:
    def __init__(self, x, y, name, xlabel, ylabel):
        date = datetime.date.today()
        plt.plot(x,y)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(f"{name} Report")
        plt.savefig(f"./images/reports/{name}Report/{date}")
        plt.close()
