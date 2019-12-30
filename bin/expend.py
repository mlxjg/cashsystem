from ui import expendui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QRegExp,QDate,QDateTime
from PyQt5.QtGui import QRegExpValidator
import time,random
from config import Config_set
class Expend_system(QMainWindow,expendui.Ui_MainWindow,Config_set):
    def __init__(self):
        super(Expend_system, self).__init__()
        self.setupUi(self)
        self.ZC_date_set = time.localtime()
        self.ZC_date.setDateTime(QDateTime(QDate(self.ZC_date_set[0], self.ZC_date_set[1],self.ZC_date_set[2])))
        print(self.ZC_date)
        # 为Qlineedit添加正则，只允许输入数字
        Qreg = QRegExp("[0-9\.]+$")
        ipValidator = QRegExpValidator(Qreg)
        self.ZC_cash.setValidator(ipValidator)
        self.ZC_TJ_button.clicked.connect(self.ZC_expend_func)
    def ZC_expend_func(self):
        self.MYSQL_conn()
        for i in range(0, 10):
            nowTime = time.strftime("%H%M%S")  # 生成当前时间
            randomNum = random.randint(1, 99)  # 生成的随机整数n，其中0<=n<=100
            uniqueNum = str(nowTime) + str(randomNum)
        date = self.ZC_date.text()
        cash = self.ZC_cash.text()
        category = self.ZC_leibie.currentText()
        remarks = self.ZC_beizhu.text()
        sql = """insert into Expend_table (ID,E_date,E_cash,E_category,E_remarks) \
         values ("%s","%s","%s","%s","%s")"""  % (uniqueNum,date,cash,category,remarks)
        try:
            self.cur.execute(sql)  # 像sql语句传递参数
            # 提交
            self.conn.commit()
        except Exception as e:
            # 错误回滚
            self.conn.rollback()
        self.conn.close()
        self.ZC_cash.clear()
        self.ZC_beizhu.clear()

