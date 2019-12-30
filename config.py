import pymysql

class Config_set:
    def __init__(self):
        pass
    def MYSQL_conn(self):
        self.conn = pymysql.connect(host='********', port=3306, user='*****', passwd='*****', db='*****',charset='utf8')
        #创建游标
        self.cur = self.conn.cursor()

    # 设置门店名
    def Mendian(self):
        self.mendian = "闲林店"

    # 设置TITLE
    def Windows_title_set_func(self):
        self.setWindowTitle("HE服装收银系统")

    # 设置系统名
    def System_name(self):
        System_name = "HE服装收银系统"
        return System_name