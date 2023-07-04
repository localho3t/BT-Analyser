import datetime
import matplotlib.pyplot as plt

class TraficReportCreator:
    date = datetime.date.today()
    def create(self,data):
        time_dict = {}
        for time in data['time']:
            hour, minute, second = time.split(':')[:3]
            hour = int(hour)
            if hour < 10:
                hour = '0' + str(hour)
            time_dict.setdefault(f"{hour}", 0)
            time_dict[f"{hour}"] += 1

        duplicates = {k: v for k, v in time_dict.items() if v > 0}
        plt.plot(duplicates.keys(), duplicates.values())
        plt.xlabel('Time')
        plt.ylabel('volumns')
        plt.title('Trafic Report')
        plt.savefig(f"./images/reports/traficReport/{self.date}")
        plt.close()
