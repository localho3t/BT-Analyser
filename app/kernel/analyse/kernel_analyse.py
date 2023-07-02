class KernelAnalyser:
    data = None

    def setDate(self, data):
        self.data = data
        self.Intersection()

    def Intersection(self):
        ip_address = []
        timestamp = []
        date = []
        time = []
        request = []
        status_code = []
        response_size = []
        referrer = []
        user_agent = []
        from app.kernel.analyse.check_method.method_app import method_analyse
        from app.kernel.analyse.check_response.check_reponse_app import CheckResponseApp
        cra = CheckResponseApp()
        for i in self.data:
            ip_address.append(i['ip_address'])
            timestamp.append(i['timestamp'])
            date.append(i['date'])
            time.append(i['time'])
            request.append(i['request'])
            status_code.append(i['status_code'])
            response_size.append(i['response_size'])
            referrer.append(i['referrer'])
            user_agent.append(i['user_agent'])

        method_result = method_analyse(request)
        response_result = cra.setData(status_code)
        # print(response_result)
