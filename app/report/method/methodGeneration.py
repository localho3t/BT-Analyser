from app.report.generate.gen import ReportGenerate


class MethodReportCreator:
    def create(self, data):
        ReportGenerate(data.keys(), data.values(),
                       "method", "method", "counter")
