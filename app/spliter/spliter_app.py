import re
import datetime


class SpliterApp:
    data = []
    ip = None
    method = None
    response = None
    time = None
    date = None
    route_request = None
    response_length = 0
    other_information = None
    UserAgent = None

    def setData(self, data):
        self.data = data

    def convertTimeStamp(self, date_time):
        date_regex = r'^(\d{2})/(\w+)/(\d{4}):(\d{2}):(\d{2}):(\d{2}) (\+\d{4})$'
        date_matches = re.match(date_regex, date_time)
        day = date_matches.group(1)
        month = date_matches.group(2)
        year = date_matches.group(3)
        hour = date_matches.group(4)
        minute = date_matches.group(5)
        second = date_matches.group(6)
        date = f"{year}-{month}-{day}"
        time = f"{hour}:{minute}:{second}"
        date_string = f"{date} {time}"
        date_obj = datetime.datetime.strptime(
            date_string, '%Y-%b-%d %H:%M:%S')
        return [date_obj, time, date]

    def getInformation(self):
        regex = r'^([\d\.]+) (\S+) (\S+) \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"$'

        matches = re.match(regex, self.data)
        if matches:
            ip_address = matches.group(1)
            user_name = matches.group(2)
            auth_user = matches.group(3)
            timestamp = matches.group(4)
            timestamp = self.convertTimeStamp(timestamp)
            request = matches.group(5)
            status_code = matches.group(6)
            response_size = matches.group(7)
            referrer = matches.group(8)
            user_agent = matches.group(9)
            res = {
                'ip_address': ip_address,
                'user_name': user_name,
                'auth_user': auth_user,
                'timestamp': timestamp[0],
                'date': timestamp[2],
                'time': timestamp[1],
                'request': request,
                'status_code': status_code,
                'response_size': response_size,
                'referrer': referrer,
                'user_agent': user_agent,
            }
            return res
