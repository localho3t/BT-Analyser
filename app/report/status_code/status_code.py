from app.report.generate.gen import ReportGenerate


class StatusCodeReportCreator:
    def create(self, data):
        ReportGenerate(data.keys(), data.values(),
                       "statusCode", "status_code", "counter")
