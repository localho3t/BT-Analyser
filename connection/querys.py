class Querys:
    def select_log(self):
        return "SELECT count(*) FROM log WHERE created_at = %s limit 1"

    def insert_log(self):
        return "INSERT INTO log (response,headers,request_count,\
                        created_at,update_at,avrg_volume) \
    VALUES (%s,%s,%s,%s,%s,%s);"

    def update_log(self):
        return "UPDATE `log` SET `response` = %s , `headers` = %s , \
    `request_count` = %s , `update_at` = %s , `avrg_volume` = %s \
    WHERE `created_at` = %s "

    def select_trafic_log(self):
        return "SELECT count(*) FROM trafic_report WHERE date = %s limit 1"

    def insert_trafic_log(self):
        return "INSERT INTO trafic_report (data,date)\
        VALUES (%s,%s);"

    def update_trafic_log(self):
        return "UPDATE `trafic_report` SET `data` = %s WHERE `date` = %s "
