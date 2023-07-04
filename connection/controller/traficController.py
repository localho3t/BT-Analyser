from connection.connections import Connection
import json
import datetime
from app.report.trafic.traficReport import TraficReportCreator

class traficController(Connection):
    trc = TraficReportCreator()
    def select_insert(self, data):
        self.trc.create(data)
        date = datetime.date.today()
        sql = self.querys.select_trafic_log()
        cursor = self.mydb.cursor()
        val_select = (date,)
        cursor.execute(sql, val_select)
        myresult = cursor.fetchall()
        myresult = myresult[0][0]
        # print(myresult)
        if myresult == 0:
            sql = self.querys.insert_trafic_log()
            val = (json.dumps(data), date)
            cursor.execute(sql, val)
            self.mydb.commit()
        elif myresult == 1:
            sql = self.querys.update_trafic_log()
            val = (json.dumps(data), date)
            cursor.execute(sql, val)
            self.mydb.commit()
