from ui import statisticsui
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import QMainWindow
import time
from config import Config_set
class Statisticsui_system(QMainWindow,statisticsui.Ui_MainWindow,Config_set):
    def __init__(self,Foreground_user):
        super(Statisticsui_system, self).__init__()
        self.setupUi(self)
        #获取前台用户
        self.Foreground_user = Foreground_user
        # 销售字典
        self.C_date = time.localtime()
        self.QS_date.setDateTime(QtCore.QDateTime(QtCore.QDate(self.C_date[0], self.C_date[1],self.C_date[2]), QtCore.QTime(0, 0, 0)))
        self.JS_date.setDateTime(QtCore.QDateTime(QtCore.QDate(self.C_date[0], self.C_date[1], self.C_date[2]), QtCore.QTime(0, 0, 0)))
        self.sale_dict = {}
        self.ST_cx_button.clicked.connect(self.Current_date)

    #实现当前日期，并对当前日其内容进行检索
    def Current_date(self):
        self.MYSQL_conn()
        self.sale_dict.clear()
        QS_date = self.QS_date.text()
        QS_date =QS_date.replace("-","")
        JS_data = self.JS_date.text()
        JS_data = JS_data.replace("-","")
        JS_data = int(JS_data) +1
        sql = """SELECT * FROM Sale_list where Sale_id between '%s' and '%s'"""% (QS_date,JS_data)
        # 提交命令
        self.cur.execute(sql)
        # 返回
        data = self.cur.fetchall()
        data_num = len(data)+1
        sj_num = 0
        if sj_num <= data_num:
            for i in data:
                if i[11] == self.Foreground_user:
                    self.sale_dict[sj_num] = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]]
                    sj_num = sj_num + 1
                    self.DL_table_func()
                else:
                    pass
        self.conn.close()
    def DL_table_func(self):
        #金额变量
        sale_num_cu = 0
        sale_d_cu = ""
        sale_sl_cu = 0
        #求总销售额
        for v in self.sale_dict.values():
            sale_num_cu +=int(v[8])
            sale_sl_cu += int(v[6])
            sale_d_cu = v[10]
        self.XS_JE_line.setText(str(sale_num_cu))
        self.XS_people_line.setText(self.Foreground_user)
        self.XS_d_line.setText(sale_d_cu)
        self.XS_SL_line.setText(str(sale_sl_cu))
        buchang = 0
        if buchang < len(self.sale_dict):
            for k,v in self.sale_dict.items():
                #创建Qtable表格
                self.XS_table_w.setObjectName("XS_table_w")
                #设置列数
                self.XS_table_w.setColumnCount(7)
                #设置行数
                self.XS_table_w.setRowCount(buchang+1)
                #设置行名
                item = QtWidgets.QTableWidgetItem()
                self.XS_table_w.setVerticalHeaderItem(buchang, item)
                #设置行列标号
                item = QtWidgets.QTableWidgetItem()
                self.XS_table_w.setItem(buchang, 0, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                font = QtGui.QFont()
                font.setPointSize(12)
                item.setFont(font)

                item = QtWidgets.QTableWidgetItem()
                self.XS_table_w.setItem(buchang, 1, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                font = QtGui.QFont()
                font.setPointSize(12)
                item.setFont(font)
                item = QtWidgets.QTableWidgetItem()
                self.XS_table_w.setItem(buchang, 2, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                font = QtGui.QFont()
                font.setPointSize(12)
                item.setFont(font)
                item = QtWidgets.QTableWidgetItem()
                self.XS_table_w.setItem(buchang, 3, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                font = QtGui.QFont()
                font.setPointSize(12)
                item.setFont(font)
                item = QtWidgets.QTableWidgetItem()
                self.XS_table_w.setItem(buchang, 4, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                font = QtGui.QFont()
                font.setPointSize(12)
                item.setFont(font)
                item = QtWidgets.QTableWidgetItem()
                self.XS_table_w.setItem(buchang, 5, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                font = QtGui.QFont()
                font.setPointSize(12)
                item.setFont(font)
                item = QtWidgets.QTableWidgetItem()
                self.XS_table_w.setItem(buchang, 6, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                font = QtGui.QFont()
                font.setPointSize(12)
                item.setFont(font)
                _translate = QtCore.QCoreApplication.translate
                __sortingEnabled = self.XS_table_w.isSortingEnabled()
                self.XS_table_w.setSortingEnabled(False)

                item = self.XS_table_w.item(buchang, 0)
                item.setText(_translate("MainWindow", v[0]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.XS_table_w.item(buchang, 1)
                item.setText(_translate("MainWindow", v[1]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.XS_table_w.item(buchang, 2)
                item.setText(_translate("MainWindow", v[2]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.XS_table_w.item(buchang, 3)
                item.setText(_translate("MainWindow", v[3]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.XS_table_w.item(buchang, 4)
                item.setText(_translate("MainWindow", v[4]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.XS_table_w.item(buchang, 5)
                item.setText(_translate("MainWindow", v[6]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.XS_table_w.item(buchang, 6)
                item.setText(_translate("MainWindow", v[8]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.XS_table_w.setSortingEnabled(__sortingEnabled)
                buchang = buchang + 1
        #设置列数标记
        item = QtWidgets.QTableWidgetItem()
        self.XS_table_w.setHorizontalHeaderItem(0, item)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item = QtWidgets.QTableWidgetItem()
        self.XS_table_w.setHorizontalHeaderItem(1, item)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item = QtWidgets.QTableWidgetItem()
        self.XS_table_w.setHorizontalHeaderItem(2, item)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item = QtWidgets.QTableWidgetItem()
        self.XS_table_w.setHorizontalHeaderItem(3, item)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item = QtWidgets.QTableWidgetItem()
        self.XS_table_w.setHorizontalHeaderItem(4, item)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item = QtWidgets.QTableWidgetItem()
        self.XS_table_w.setHorizontalHeaderItem(5, item)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item = QtWidgets.QTableWidgetItem()
        self.XS_table_w.setHorizontalHeaderItem(6, item)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.XS_table_w_Table_header()

    def XS_table_w_Table_header(self):
        _translate = QtCore.QCoreApplication.translate
        item = self.XS_table_w.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "流水号"))
        item = self.XS_table_w.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "条码"))
        item = self.XS_table_w.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "名称"))
        item = self.XS_table_w.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "规格"))
        item = self.XS_table_w.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "类别"))
        item = self.XS_table_w.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "数量"))
        item = self.XS_table_w.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "金额"))


