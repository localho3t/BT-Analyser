from app.report.generate.gen import ReportGenerate
class TraficReportCreator:
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
        ReportGenerate(duplicates.keys(), duplicates.values(), "trafic","Time","volumns")
