
from ui.adminui import Ui_MainWindow
from PyQt5 import QtCore,QtWidgets


class Sstj(QtWidgets.QWidget,Ui_MainWindow):
    def __init__(self):
        super(Sstj, self).__init__()
        self.setupUi(self)

        #分类数据
        self.xstj_js_mx_dict = {}
        self.xstj_js_tj_dict = {}

    def Xstj_button_func(self):
        self.TJFX_xstj_CX_button.clicked.connect(self.Mysql_sstj_cx_func)
        self.TJFX_xstj_xstj.clicked.connect(self.XSMX_table_func)
    #实现用户输入的提示列表
    def Mysql_sstj_cx_func(self):
        self.xstj_js_mx_dict.clear()
        self.xstj_js_tj_dict.clear()
        self.MYSQL_conn()
        TJFX_xstj_starttime = self.TJFX_xstj_starttime.text()
        TJFX_xstj_starttime =TJFX_xstj_starttime.replace("-","")
        TJFX_xstj_finishtime = self.TJFX_xstj_finishtime.text()
        TJFX_xstj_finishtime = TJFX_xstj_finishtime.replace("-","")
        TJFX_xstj_finishtime = int(TJFX_xstj_finishtime) +1
        TJFX_xstj_user = self.TJFX_xstj_user.currentText()
        sql = """SELECT * FROM Sale_list where Sale_id between '%s' and '%s'"""% (TJFX_xstj_starttime,TJFX_xstj_finishtime)
        # 提交命令
        self.cur.execute(sql)
        # 返回
        data = self.cur.fetchall()
        num = 1
        sum_xs = 0
        sum_lr = 0
        if TJFX_xstj_user == "全部销售员":
            for i in data:
                self.xstj_js_mx_dict[i[0][0:8]] = {}
            for i in data:
                self.xstj_js_mx_dict[i[0][0:8]][num]= [i[1],i[2],i[3],i[6],i[8],i[9]]
                num = num +1
            for v,j in self.xstj_js_mx_dict.items():
                tj_key = v
                tj_cb = 0
                tj_xs = 0
                for y in j.values():
                    if tj_key == v:
                        tj_cb = tj_cb + int(y[5])
                        tj_xs = tj_xs + int(y[4])
                self.xstj_js_tj_dict[tj_key] = [tj_cb,tj_xs]
                tj_key = v
                tj_cb = 0
                tj_xs = 0
                sum_xs = 0
                sum_lr = 0
                for u in self.xstj_js_tj_dict.values():
                    sum_xs = sum_xs + u[1]
                    sum_lr = sum_lr + (u[1]-u[0])
            self.TJFX_xstj_xs_sum.setText(str(sum_xs))
            self.TJFX_xstj_lr_sum.setText(str(sum_lr))
        else:
            for i in data:
                if TJFX_xstj_user == i[11]:
                    self.xstj_js_mx_dict[i[0][0:8]] = {}
            for i in data:
                if TJFX_xstj_user == i[11]:
                    self.xstj_js_mx_dict[i[0][0:8]][num]= [i[1],i[2],i[3],i[6],i[8],i[9]]
                    num = num +1
            for v,j in self.xstj_js_mx_dict.items():
                tj_key = v
                tj_cb = 0
                tj_xs = 0
                for y in j.values():
                    if tj_key == v:
                        tj_cb = tj_cb + int(y[5])
                        tj_xs = tj_xs + int(y[4])

                self.xstj_js_tj_dict[tj_key] = [tj_cb,tj_xs]
                tj_key = v
                tj_cb = 0
                tj_xs = 0
                sum_xs = 0
                sum_lr = 0
                for u in self.xstj_js_tj_dict.values():
                    sum_xs = sum_xs + u[1]
                    sum_lr = sum_lr + ((u[1]-u[0]))
            self.TJFX_xstj_xs_sum.setText(str(sum_xs))
            self.TJFX_xstj_lr_sum.setText(str(sum_lr))

        self.XSTJ_table_func()

    def XSTJ_table_func(self):
        self.TJFX_xstj_xstj.clearContents()
        buchang = 0
        if buchang <= len(self.xstj_js_tj_dict):
            for k, v in self.xstj_js_tj_dict.items():
                 # 创建Qtable表格
                 self.TJFX_xstj_xstj.setObjectName("TJFX_xstj_xstj")
                 # 设置列数
                 self.TJFX_xstj_xstj.setColumnCount(3)
                 # 设置行数
                 self.TJFX_xstj_xstj.setRowCount(buchang + 1)
                 # 设置行名
                 item = QtWidgets.QTableWidgetItem()
                 self.TJFX_xstj_xstj.setVerticalHeaderItem(buchang, item)
                 # 设置行列标号
                 item = QtWidgets.QTableWidgetItem()
                 self.TJFX_xstj_xstj.setItem(buchang, 0, item)
                 item.setFlags(
                     QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                 item = QtWidgets.QTableWidgetItem()
                 self.TJFX_xstj_xstj.setItem(buchang, 1, item)
                 item.setFlags(
                     QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                 item = QtWidgets.QTableWidgetItem()
                 self.TJFX_xstj_xstj.setItem(buchang, 2, item)
                 item.setFlags(
                     QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                 # 设置列数标记
                 item = QtWidgets.QTableWidgetItem()
                 self.TJFX_xstj_xstj.setHorizontalHeaderItem(0, item)
                 item = QtWidgets.QTableWidgetItem()
                 self.TJFX_xstj_xstj.setHorizontalHeaderItem(1, item)
                 item = QtWidgets.QTableWidgetItem()
                 self.TJFX_xstj_xstj.setHorizontalHeaderItem(2, item)

                 _translate = QtCore.QCoreApplication.translate
                 __sortingEnabled = self.SPGL_sqll_table.isSortingEnabled()
                 self.TJFX_xstj_xstj.setSortingEnabled(False)
                 item = self.TJFX_xstj_xstj.item(buchang, 0)
                 key = "%s-%s-%s"%(k[0:4],k[4:6],k[6:8])
                 item.setText(_translate("MainWindow", str(key)))
                 item.setTextAlignment(QtCore.Qt.AlignCenter)
                 item = self.TJFX_xstj_xstj.item(buchang, 1)
                 item.setText(_translate("MainWindow", str(v[1])))
                 item.setTextAlignment(QtCore.Qt.AlignCenter)
                 item = self.TJFX_xstj_xstj.item(buchang, 2)
                 item.setText(_translate("MainWindow", str(v[1]-v[0])))
                 item.setTextAlignment(QtCore.Qt.AlignCenter)
                 buchang = buchang +1
            self.XSTJ_header_table()

    def XSTJ_header_table(self):
        _translate = QtCore.QCoreApplication.translate
        item = self.TJFX_xstj_xstj.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "日期"))
        item = self.TJFX_xstj_xstj.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "销售额"))
        item = self.TJFX_xstj_xstj.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "毛利润"))


    def XSMX_table_func(self):
        try:
            row_select = self.TJFX_xstj_xstj.selectedItems()
            row_id = row_select[0].text()
            row_id = row_id[0:4]+row_id[5:7]+ row_id[8:10]
            row = row_select[0].text()
            buchang = 0
            if buchang <= len(self.xstj_js_mx_dict):
                for k, v in self.xstj_js_mx_dict.items():
                     if k == row_id:
                         for x in v.values():
                             # 创建Qtable表格
                             self.TJFX_xstj_xsmx.setObjectName("TJFX_xstj_xsmx")
                             # 设置列数
                             self.TJFX_xstj_xsmx.setColumnCount(5)
                             # 设置行数
                             self.TJFX_xstj_xsmx.setRowCount(buchang + 1)
                             # 设置行名
                             item = QtWidgets.QTableWidgetItem()
                             self.TJFX_xstj_xsmx.setVerticalHeaderItem(buchang, item)
                             # 设置行列标号
                             item = QtWidgets.QTableWidgetItem()
                             self.TJFX_xstj_xsmx.setItem(buchang, 0, item)
                             item.setFlags(
                                 QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                             item = QtWidgets.QTableWidgetItem()
                             self.TJFX_xstj_xsmx.setItem(buchang, 1, item)
                             item.setFlags(
                                 QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                             item = QtWidgets.QTableWidgetItem()
                             self.TJFX_xstj_xsmx.setItem(buchang, 2, item)
                             item.setFlags(
                                 QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                             item = QtWidgets.QTableWidgetItem()
                             self.TJFX_xstj_xsmx.setItem(buchang, 3, item)
                             item.setFlags(
                                 QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                             item = QtWidgets.QTableWidgetItem()
                             self.TJFX_xstj_xsmx.setItem(buchang, 4, item)
                             item.setFlags(
                                 QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                             # 设置列数标记
                             item = QtWidgets.QTableWidgetItem()
                             self.TJFX_xstj_xsmx.setHorizontalHeaderItem(0, item)
                             item = QtWidgets.QTableWidgetItem()
                             self.TJFX_xstj_xsmx.setHorizontalHeaderItem(1, item)
                             item = QtWidgets.QTableWidgetItem()
                             self.TJFX_xstj_xsmx.setHorizontalHeaderItem(2, item)
                             item = QtWidgets.QTableWidgetItem()
                             self.TJFX_xstj_xsmx.setHorizontalHeaderItem(3, item)
                             item = QtWidgets.QTableWidgetItem()
                             self.TJFX_xstj_xsmx.setHorizontalHeaderItem(4, item)

                             _translate = QtCore.QCoreApplication.translate
                             __sortingEnabled = self.SPGL_sqll_table.isSortingEnabled()
                             self.TJFX_xstj_xsmx.setSortingEnabled(False)
                             item = self.TJFX_xstj_xsmx.item(buchang, 0)
                             item.setText(_translate("MainWindow", x[0]))
                             item.setTextAlignment(QtCore.Qt.AlignCenter)
                             item = self.TJFX_xstj_xsmx.item(buchang, 1)
                             item.setText(_translate("MainWindow", x[1]))
                             item.setTextAlignment(QtCore.Qt.AlignCenter)
                             item = self.TJFX_xstj_xsmx.item(buchang, 2)
                             item.setText(_translate("MainWindow", x[2]))
                             item.setTextAlignment(QtCore.Qt.AlignCenter)
                             item = self.TJFX_xstj_xsmx.item(buchang, 3)
                             item.setText(_translate("MainWindow", x[3]))
                             item.setTextAlignment(QtCore.Qt.AlignCenter)
                             item = self.TJFX_xstj_xsmx.item(buchang, 4)
                             item.setText(_translate("MainWindow", x[4]))
                             item.setTextAlignment(QtCore.Qt.AlignCenter)
                             buchang = buchang +1
        except KeyError:
            pass
        self.XSMX_header_table()

    def XSMX_header_table(self):
        _translate = QtCore.QCoreApplication.translate
        item = self.TJFX_xstj_xsmx.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "货号"))
        item = self.TJFX_xstj_xsmx.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "名称"))
        item = self.TJFX_xstj_xsmx.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "规格"))
        item = self.TJFX_xstj_xsmx.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "数量"))
        item = self.TJFX_xstj_xsmx.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "金额"))









