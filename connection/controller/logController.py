from connection.connections import Connection
import json
import datetime


class logController(Connection):
    def select_insert(self, data):
        sql = self.querys.select_log()
        cursor = self.mydb.cursor()
        date = data['date']
        method_result = data['method_result']
        response_result = data['response_result']
        response_size_avrg = data['response_size_avrg']
        request_count = data['request_count']
        val_select = (
            date,
        )
        cursor.execute(sql, val_select)
        myresult = cursor.fetchall()
        myresult = myresult[0][0]
        if myresult == 0:
            sql = self.querys.insert_log()
            val = (
                str(json.dumps(response_result)),
                str(json.dumps(method_result)),
                request_count,
                date,
                datetime.datetime.now(),
                response_size_avrg,
            )
            cursor.execute(sql, val)
            self.mydb.commit()
        elif myresult == 1:
            sql = self.querys.update_log()
            val = (
                str(json.dumps(response_result)),
                str(json.dumps(method_result)),
                request_count,
                datetime.datetime.now(),
                response_size_avrg,
                date,
            )
            cursor.execute(sql, val)
            self.mydb.commit()
