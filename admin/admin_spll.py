
from ui.adminui import Ui_MainWindow
from PyQt5 import QtCore,QtWidgets


class Spll(QtWidgets.QWidget,Ui_MainWindow):
    def __init__(self):
        super(Spll, self).__init__()
        self.setupUi(self)
        self.LL_dict = {}

    #实现用户输入的提示列表
    def Mysql_spll_cx(self):
        self.MYSQL_conn()
        sql = """SELECT * FROM SP_List"""
        # 提交命令
        self.cur.execute(sql)
        # 返回
        data = self.cur.fetchall()
        data_num = len(data)+1
        sj_num = 1
        if sj_num <= data_num:
            for i in data:
                self.LL_dict[sj_num] =  [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]]
                sj_num = sj_num + 1
        self.conn.close()
        self.SPLL_table_func()

    def SPLL_table_func(self):
        buchang = 0
        if buchang < len(self.LL_dict):
            for k, v in self.LL_dict.items():
                # 创建Qtable表格
                self.SPGL_sqll_table.setObjectName("SPGL_sqll_table")
                # 设置列数
                self.SPGL_sqll_table.setColumnCount(11)
                # 设置行数
                self.SPGL_sqll_table.setRowCount(buchang + 1)
                # 设置行名
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setVerticalHeaderItem(buchang, item)
                # 设置行列标号
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setItem(buchang, 0, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setItem(buchang, 1, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setItem(buchang, 2, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setItem(buchang, 3, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setItem(buchang, 4, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setItem(buchang, 5, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setItem(buchang, 6, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setItem(buchang, 7, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setItem(buchang, 8, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setItem(buchang, 9, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setItem(buchang, 10, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)

                # 设置列数标记
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setHorizontalHeaderItem(5, item)
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setHorizontalHeaderItem(6, item)
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setHorizontalHeaderItem(7, item)
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setHorizontalHeaderItem(8, item)
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setHorizontalHeaderItem(9, item)
                item = QtWidgets.QTableWidgetItem()
                self.SPGL_sqll_table.setHorizontalHeaderItem(10, item)

                _translate = QtCore.QCoreApplication.translate
                __sortingEnabled = self.SPGL_sqll_table.isSortingEnabled()
                self.SPGL_sqll_table.setSortingEnabled(False)
                item = self.SPGL_sqll_table.item(buchang, 0)
                item.setText(_translate("MainWindow", str(k)))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.SPGL_sqll_table.item(buchang, 1)
                item.setText(_translate("MainWindow", v[0]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.SPGL_sqll_table.item(buchang, 2)
                item.setText(_translate("MainWindow", v[1]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.SPGL_sqll_table.item(buchang, 3)
                item.setText(_translate("MainWindow", v[2]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.SPGL_sqll_table.item(buchang, 4)
                item.setText(_translate("MainWindow", v[3]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.SPGL_sqll_table.item(buchang, 5)
                item.setText(_translate("MainWindow", v[4]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.SPGL_sqll_table.item(buchang, 6)
                item.setText(_translate("MainWindow", v[5]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.SPGL_sqll_table.item(buchang, 7)
                item.setText(_translate("MainWindow", v[6]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.SPGL_sqll_table.item(buchang, 8)
                item.setText(_translate("MainWindow", v[7]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.SPGL_sqll_table.item(buchang, 9)
                item.setText(_translate("MainWindow", v[8]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.SPGL_sqll_table.item(buchang, 10)
                item.setText(_translate("MainWindow", v[9]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.SPGL_sqll_table.setSortingEnabled(__sortingEnabled)
                buchang = buchang + 1
            self.header_table()

    def header_table(self):
         _translate = QtCore.QCoreApplication.translate
         item = self.SPGL_sqll_table.horizontalHeaderItem(0)
         item.setText(_translate("MainWindow", "序号"))
         item = self.SPGL_sqll_table.horizontalHeaderItem(1)
         item.setText(_translate("MainWindow", "货号"))
         item = self.SPGL_sqll_table.horizontalHeaderItem(2)
         item.setText(_translate("MainWindow", "名称"))
         item = self.SPGL_sqll_table.horizontalHeaderItem(3)
         item.setText(_translate("MainWindow", "规格"))
         item = self.SPGL_sqll_table.horizontalHeaderItem(4)
         item.setText(_translate("MainWindow", "类别"))
         item = self.SPGL_sqll_table.horizontalHeaderItem(5)
         item.setText(_translate("MainWindow", "库存"))
         item = self.SPGL_sqll_table.horizontalHeaderItem(6)
         item.setText(_translate("MainWindow", "售出"))
         item = self.SPGL_sqll_table.horizontalHeaderItem(7)
         item.setText(_translate("MainWindow", "单位"))
         item = self.SPGL_sqll_table.horizontalHeaderItem(8)
         item.setText(_translate("MainWindow", "零售价"))
         item = self.SPGL_sqll_table.horizontalHeaderItem(9)
         item.setText(_translate("MainWindow", "进价"))
         item = self.SPGL_sqll_table.horizontalHeaderItem(10)
         item.setText(_translate("MainWindow", "供应商"))

