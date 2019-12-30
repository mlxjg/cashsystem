from ui.adminui import Ui_MainWindow
from PyQt5.QtCore import Qt,QCoreApplication
from PyQt5.QtWidgets import QHeaderView,QWidget,QTableWidgetItem
from PyQt5.QtGui import QFont


class Zctj(QWidget,Ui_MainWindow):
    def __init__(self):
        super(Zctj, self).__init__()
        self.setupUi(self)
        self.zctj_js_mx_dict = {}
        self.zctj_js_tj_dict = {}

    def Zctj_button_func(self):
        self.EXPEND_xstj_CX_button.clicked.connect(self.Mysql_zctj_cx_func)

    def Mysql_zctj_cx_func(self):
        self.zctj_js_mx_dict.clear()

        self.zctj_js_tj_dict.clear()
        self.MYSQL_conn()
        ZCFX_xstj_starttime = self.EXPEND_xstj_starttime.text()
        ZCFX_xstj_finishtime = self.EXPEND_xstj_finishtime.text()+1
        sql = """SELECT * FROM Expend_table where E_date between '%s' and '%s'"""% (ZCFX_xstj_starttime,ZCFX_xstj_finishtime)
        # 提交命令
        self.cur.execute(sql)
        # 返回
        data = self.cur.fetchall()
        ZCFXNAME = self.ZCFX_xstj_name.currentText()
        if ZCFXNAME == "全部类别":
            for i in data:
                data = str(i[1]).replace(",","-")
                self.zctj_js_mx_dict[i[0]] = [data,i[2],i[3],i[4]]

        else:
            for x in data:
                if ZCFXNAME == x[2]:
                    data = str(x[1]).replace(",", "-")
                    self.zctj_js_mx_dict[x[0]] = [data, x[2], x[3], x[4]]
        self.ZCTJ_table_func()

    def ZCTJ_table_func(self):
        self.Expend_table.clearContents()
        self.EXPEND_xstj_lr_sum.clear()
        buchang = 0
        sum = 0
        if buchang <= len(self.zctj_js_mx_dict):
            for k, v in self.zctj_js_mx_dict.items():
                # 创建Qtable表格
                self.Expend_table.setObjectName("Expend_table")
                font = QFont()
                font.setPointSize(14)
                self.Expend_table.setFont(font)
                self.Expend_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                # 设置列数
                self.Expend_table.setColumnCount(4)
                # 设置行数
                self.Expend_table.setRowCount(buchang + 1)
                # 设置行名
                item = QTableWidgetItem()
                self.Expend_table.setVerticalHeaderItem(buchang, item)
                # 设置行列标号
                item = QTableWidgetItem()
                self.Expend_table.setItem(buchang, 0, item)
                item = QTableWidgetItem()
                self.Expend_table.setItem(buchang, 1, item)
                item = QTableWidgetItem()
                self.Expend_table.setItem(buchang, 2, item)
                item = QTableWidgetItem()
                self.Expend_table.setItem(buchang, 3, item)
                # 设置列数标记
                item = QTableWidgetItem()
                self.Expend_table.setHorizontalHeaderItem(0, item)
                item = QTableWidgetItem()
                self.Expend_table.setHorizontalHeaderItem(1, item)
                item = QTableWidgetItem()
                self.Expend_table.setHorizontalHeaderItem(2, item)
                item = QTableWidgetItem()
                self.Expend_table.setHorizontalHeaderItem(3, item)
                _translate = QCoreApplication.translate
                __sortingEnabled = self.SPGL_sqll_table.isSortingEnabled()
                self.Expend_table.setSortingEnabled(False)
                item = self.Expend_table.item(buchang, 0)
                item.setText(_translate("MainWindow", v[0]))
                item.setTextAlignment(Qt.AlignCenter)
                item = self.Expend_table.item(buchang, 1)
                item.setText(_translate("MainWindow", v[1]))
                item.setTextAlignment(Qt.AlignCenter)
                item = self.Expend_table.item(buchang, 2)
                item.setText(_translate("MainWindow", v[2]))
                item.setTextAlignment(Qt.AlignCenter)
                item = self.Expend_table.item(buchang, 3)
                item.setText(_translate("MainWindow", v[3]))
                item.setTextAlignment(Qt.AlignCenter)
                sum = sum +float(v[2])
                buchang = buchang + 1
            self.ZCTJ_header_table()
        self.EXPEND_xstj_lr_sum.setText(str(sum))


    def ZCTJ_header_table(self):
        _translate = QCoreApplication.translate
        item = self.Expend_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "日期"))
        item = self.Expend_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "内容"))
        item = self.Expend_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "金额"))
        item = self.Expend_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "备注"))


