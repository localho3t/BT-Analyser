import json


class CheckResponseApp:
    data = None

    def generate_list(self):
        lists = {
            100: 0,
            101: 0,
            102: 0,
            103: 0,
            200: 0,
            201: 0,
            202: 0,
            203: 0,
            204: 0,
            205: 0,
            206: 0,
            207: 0,
            208: 0,
            226: 0,
            300: 0,
            301: 0,
            302: 0,
            303: 0,
            304: 0,
            305: 0,
            306: 0,
            307: 0,
            308: 0,
            400: 0,
            401: 0,
            402: 0,
            403: 0,
            404: 0,
            405: 0,
            406: 0,
            407: 0,
            408: 0,
            409: 0,
            410: 0,
            411: 0,
            412: 0,
            413: 0,
            414: 0,
            415: 0,
            416: 0,
            417: 0,
            418: 0,
            419: 0,
            421: 0,
            422: 0,
            423: 0,
            424: 0,
            426: 0,
            428: 0,
            429: 0,
            431: 0,
            451: 0,
            499: 0,
            500: 0,
            501: 0,
            502: 0,
            503: 0,
            504: 0,
            505: 0,
            506: 0,
            507: 0,
            508: 0,
            510: 0,
            511: 0,
        }
        return lists

    def setData(self, data):
        self.data = data
        res = self.check_reponses()
        return res

    def check_reponses(self):
        list_ = self.generate_list()

        try:
            for i in self.data:
                c = int(i)
                list_[c] += 1
        except:
            pass
        # print(list(list_.keys()))
        # exit()
        for key in list(list_.keys()):
            if list_[key] == 0:
                list_.pop(key)
        # print(list_)
        # exit()
        return list_
