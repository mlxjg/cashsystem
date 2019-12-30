from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtCore import QDateTime,QDate,QTime,QCoreApplication
import time,sys
from admin.admin_splr import Spgl
from admin.admin_spll import Spll
from admin.admin_xstj import Sstj
from admin.admin_zctj import Zctj
from config import Config_set
class Admin_main(QMainWindow,Spgl,Spll,Sstj,Zctj,Config_set):
    def __init__(self):
        super(Admin_main, self).__init__()
        self.Windows_title_set_func()
        #设置系统名
        System_name = self.System_name()
        self.label_2.setText(System_name)
        self.label.setText(System_name)
        self.Admin_SPGL_LR.clicked.connect(self.Admin_SPGL_LR_func)
        self.Admin_SPGL_LL.clicked.connect(self.Admin_SPGL_LL_func)
        self.Admin_HYGL_LR.clicked.connect(self.Admin_HYGL_LR_func)
        self.Admin_HYGL_LL.clicked.connect(self.Admin_HYGL_LL_func)
        self.Admin_YHGL_XTYH.clicked.connect(self.Admin_YHGL_XTYH_func)
        self.Admin_YHGL_YGGL.clicked.connect(self.Admin_YHGL_YGGL_func)
        self.Admin_YHGL_YGYJ.clicked.connect(self.Admin_YHGL_YGYJ_func)
        self.Admin_TJFX_XSTJ.clicked.connect(self.Admin_TJFX_XSTJ_func)
        self.Admin_TJFX_KCTJ.clicked.connect(self.Admin_TJFX_KCTJ_func)
        self.Admin_TJFX_JYFX.clicked.connect(self.Admin_TJFX_JYFX_func)
        self.Admin_XTSZ_XTSZ.clicked.connect(self.Admin_XTSZ_XTSZ_func)
        self.Admin_XTGL_GYRJ.clicked.connect(self.Admin_XTGL_GYRJ_func)
        self.Admin_TJFX_ZCTJ.clicked.connect(self.Admin_TJFX_ZCTJ_func)

        self.Initialization_func()

    def Initialization_func(self):
        # 销售统计设置起始日期
        self.time_date = time.localtime()
        self.TJFX_xstj_starttime.setDateTime(QDateTime(QDate(self.time_date[0], self.time_date[1],self.time_date[2]), QTime(0, 0, 0)))
        self.TJFX_xstj_finishtime.setDateTime(QDateTime(QDate(self.time_date[0], self.time_date[1], self.time_date[2]), QTime(0, 0, 0)))
        self.EXPEND_xstj_starttime.setDateTime(QDateTime(QDate(self.time_date[0], self.time_date[1],self.time_date[2]), QTime(0, 0, 0)))
        self.EXPEND_xstj_finishtime.setDateTime(QDateTime(QDate(self.time_date[0], self.time_date[1], self.time_date[2]), QTime(0, 0, 0)))

        #初始化销售统计内的名字列表
        user_list = []
        self.MYSQL_conn()
        sql = """SELECT User_name FROM User_table """
        # 提交命令
        self.cur.execute(sql)
        # 返回
        data = self.cur.fetchall()
        sql_data_num = 1
        _translate = QCoreApplication.translate
        self.TJFX_xstj_user.addItem("")
        self.TJFX_xstj_user.setItemText(0, _translate("MainWindow", "全部销售员"))
        if sql_data_num <= len(data):
            for i in data:
                self.TJFX_xstj_user.addItem("")
                self.TJFX_xstj_user.setItemText(sql_data_num, _translate("MainWindow", i[0]))
                sql_data_num = sql_data_num + 1
        self.conn.close()
    def Admin_SPGL_LR_func(self):
        self.Spgl_sprk_button()
        self.Display_layer.setCurrentIndex(1)
    def Admin_SPGL_LL_func(self):
        self.Display_layer.setCurrentIndex(2)
        self.Mysql_spll_cx()

    def Admin_HYGL_LR_func(self):
        self.Display_layer.setCurrentIndex(3)
    def Admin_HYGL_LL_func(self):
        self.Display_layer.setCurrentIndex(4)
    def Admin_YHGL_XTYH_func(self):
        self.Display_layer.setCurrentIndex(5)
    def Admin_YHGL_YGGL_func(self):
        self.Display_layer.setCurrentIndex(6)
    def Admin_YHGL_YGYJ_func(self):

        self.Display_layer.setCurrentIndex(7)
    def Admin_TJFX_XSTJ_func(self):
        self.Display_layer.setCurrentIndex(9)
        self.Xstj_button_func()
    def Admin_TJFX_KCTJ_func(self):
        self.Display_layer.setCurrentIndex(8)
    def Admin_TJFX_JYFX_func(self):
        self.Display_layer.setCurrentIndex(10)
    def Admin_XTSZ_XTSZ_func(self):
        self.Display_layer.setCurrentIndex(11)

    def Admin_XTGL_GYRJ_func(self):

        self.Display_layer.setCurrentIndex(12)

    def Admin_TJFX_ZCTJ_func(self):
        self.Display_layer.setCurrentIndex(11)
        self.Zctj_button_func()

if __name__ == "__main__":
    app =  QApplication(sys.argv)
    try:
        win = Admin_main()
        win.show()
    except AttributeError:
        print("key")
    except ValueError:
        print("key")

    sys.exit(app.exec_())
