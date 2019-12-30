from ui import returnbackui
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow,QCompleter,QMenu
from PyQt5 import QtCore,QtWidgets,QtGui
import time
from config import Config_set
class Returnback_system(QMainWindow,returnbackui.Ui_mainWindow,Config_set):
    def __init__(self,Foreground_user):
        super(Returnback_system, self).__init__()
        self.setupUi(self)
        self.Mendian()
        self.LS_num_func()
        self.Foreground_user = Foreground_user
        # 设置右击菜单
        self.TH_table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.TH_table.customContextMenuRequested.connect(self.showContextMenu_TH)
        self.RE_GWXC_button.clicked.connect(self.GW_time_func)
        self.RE_LSCX_button.clicked.connect(self.LS_CX_func)
        self.TH_dict = {}
        #设置起始日期
        self.C_date = time.localtime()
        self.RE_GWQS_date.setDateTime(QtCore.QDateTime(QtCore.QDate(self.C_date[0], self.C_date[1],self.C_date[2]), QtCore.QTime(0, 0, 0)))
        self.RE_GWJS_date.setDateTime(QtCore.QDateTime(QtCore.QDate(self.C_date[0], self.C_date[1], self.C_date[2]), QtCore.QTime(0, 0, 0)))
        self.RE_TJ_button.clicked.connect(self.SJ_CZ_func)
        self.show()
    #流水号补全方法
    def LS_num_func(self):
        self.MYSQL_conn()
        # 设置补全列表
        Intelligent_input_list = []
        # 查询语句
        sql = """SELECT Sale_id FROM Sale_list"""
        # 提交命令
        self.cur.execute(sql)
        # 返回烽据
        data = self.cur.fetchall()
        # 遍历结果
        for x in data:
            Intelligent_input_list.append(x[0])
        self.conn.close
        # 加载补全列表
        self.xlist = QCompleter(Intelligent_input_list)
        # 增加自动补全
        self.RE_LSCX_text.setCompleter(self.xlist)
        # 设置匹配模式  有三种： Qt.MatchStartsWith 开头匹配（默认）  Qt.MatchContains 内容匹配  Qt.MatchEndsWith 结尾匹配
        self.xlist.setFilterMode(QtCore.Qt.MatchContains)
        # 设置补全模式  有三种： QCompleter.PopupCompletion（默认）  QCompleter.InlineCompletion   QCompleter.UnfilteredPopupCompletion
        self.xlist.setCompletionMode(QCompleter.PopupCompletion)
        # 给lineedit设置补全器
        self.RE_LSCX_text.setCompleter(self.xlist)
        # 给lineedit汪加回车确认
        #self.RE_LSCX_text.returnPressed.connect(self.Serializemap)
        # 为Qlineedit添加正则，只允许输入数字
        Qreg = QtCore.QRegExp("[0-9\.]+$")
        ipValidator = QRegExpValidator(Qreg)
        self.RE_LSCX_text.setValidator(ipValidator)
    #读取流水号数据
    def LS_CX_func(self):
        self.TH_dict.clear()
        self.MYSQL_conn()
        user_input_id = self.RE_LSCX_text.text()
        # 查询语句
        sql = "SELECT * FROM Sale_list WHERE Sale_id = '%s'" % user_input_id
        # 提交命令
        self.cur.execute(sql)
        # 返回数据
        data = self.cur.fetchall()
        # 遍历结果
        data_num = len(data)+1
        sj_num = 0
        if sj_num < data_num:
            for i in data:
                self.TH_dict[sj_num] =  [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                sj_num = sj_num + 1
        self.conn.close
        self.DL_table_func()
    #读取查询时间方法
    def GW_time_func(self):
        self.TH_dict.clear()
        self.MYSQL_conn()
        RE_GWQS_date = self.RE_GWQS_date.text()
        RE_GWQS_date =RE_GWQS_date.replace("-","")
        RE_GWJS_date = self.RE_GWJS_date.text()
        RE_GWJS_date = RE_GWJS_date.replace("-","")
        RE_GWJS_date = int(RE_GWJS_date) +1
        sql = """SELECT * FROM Sale_list where Sale_id between '%s' and '%s'"""% (RE_GWQS_date,RE_GWJS_date)
        # 提交命令
        self.cur.execute(sql)
        # 返回
        data = self.cur.fetchall()
        data_num = len(data)+1
        sj_num = 1
        if sj_num <= data_num:
            for i in data:
                self.TH_dict[sj_num] =  [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                sj_num = sj_num + 1
        self.conn.close
        self.DL_table_func()

    #设置底栏的内容显示
    def DL_table_func(self):
        # 金额变量
        sale_num_cu = 0
        sale_sl_cu = 0
        # 求总销售额
        for v in self.TH_dict.values():
            sale_num_cu += int(v[8])
            sale_sl_cu += int(v[6])
        self.TH_je_line.setText(str(sale_num_cu))
        self.TH_people_line.setText(self.Foreground_user)
        self.TH_d_line.setText(self.mendian)
        self.TH_sl_line.setText(str(sale_sl_cu))
        self.X_table_func()
    def showContextMenu_TH(self, pos):
        # 计算有多少条数据，默认-1,
        row_num = -1
        for i in self.TH_table.selectionModel().selection().indexes():
            row_num = i.row()
        # 表格中只有两条有效数据，所以只在前两行支持右键弹出菜单
        if row_num < 16:
            menu = QMenu()
            item1 = menu.addAction(u'删除')
            action = menu.exec_(self.TH_table.mapToGlobal(pos))
            # 设置删除内容行
            if action == item1:
                row_select = self.TH_table.selectedItems()
                id = row_select[0].text()
                row = row_select[0].text()
                id = int(id)
                del self.TH_dict[id]
                # 清除表格内容
                self.TH_table.clearContents()
                self.DL_table_func()
                self.X_table_func()
    #建表
    def X_table_func(self):
        buchang = 0
        if buchang < len(self.TH_dict):
            for k, v in self.TH_dict.items():
                # 创建Qtable表格
                self.TH_table.setObjectName("TH_table")
                # 设置列数
                self.TH_table.setColumnCount(9)
                # 设置行数
                self.TH_table.setRowCount(buchang + 1)
                # 设置行名
                item = QtWidgets.QTableWidgetItem()
                self.TH_table.setVerticalHeaderItem(buchang, item)
                # 设置行列标号
                item = QtWidgets.QTableWidgetItem()
                self.TH_table.setItem(buchang, 0, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item = QtWidgets.QTableWidgetItem()
                self.TH_table.setItem(buchang, 1, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item = QtWidgets.QTableWidgetItem()
                self.TH_table.setItem(buchang, 2, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item = QtWidgets.QTableWidgetItem()
                self.TH_table.setItem(buchang, 3, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item = QtWidgets.QTableWidgetItem()
                self.TH_table.setItem(buchang, 4, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item = QtWidgets.QTableWidgetItem()
                self.TH_table.setItem(buchang, 5, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item = QtWidgets.QTableWidgetItem()
                self.TH_table.setItem(buchang, 6, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item = QtWidgets.QTableWidgetItem()
                self.TH_table.setItem(buchang, 7, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item = QtWidgets.QTableWidgetItem()
                self.TH_table.setItem(buchang, 8, item)
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                font = QtGui.QFont()
                font.setPointSize(12)
                item.setFont(font)
                # 设置列数标记
                item = QtWidgets.QTableWidgetItem()
                self.TH_table.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.TH_table.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.TH_table.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.TH_table.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.TH_table.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.TH_table.setHorizontalHeaderItem(5, item)
                item = QtWidgets.QTableWidgetItem()
                self.TH_table.setHorizontalHeaderItem(6, item)
                item = QtWidgets.QTableWidgetItem()
                self.TH_table.setHorizontalHeaderItem(7, item)
                item = QtWidgets.QTableWidgetItem()
                self.TH_table.setHorizontalHeaderItem(8, item)

                _translate = QtCore.QCoreApplication.translate
                __sortingEnabled = self.TH_table.isSortingEnabled()
                self.TH_table.setSortingEnabled(False)
                item = self.TH_table.item(buchang, 0)
                item.setText(_translate("MainWindow", str(k)))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.TH_table.item(buchang, 1)
                item.setText(_translate("MainWindow", v[0]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.TH_table.item(buchang, 2)
                item.setText(_translate("MainWindow", v[1]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.TH_table.item(buchang, 3)
                item.setText(_translate("MainWindow", v[2]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.TH_table.item(buchang, 4)
                item.setText(_translate("MainWindow", v[3]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.TH_table.item(buchang, 5)
                item.setText(_translate("MainWindow", v[6]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.TH_table.item(buchang, 6)
                item.setText(_translate("MainWindow", v[5]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.TH_table.item(buchang, 7)
                item.setText(_translate("MainWindow", v[7]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item = self.TH_table.item(buchang, 8)
                item.setText(_translate("MainWindow", v[8]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.TH_table.setSortingEnabled(__sortingEnabled)
                buchang = buchang + 1
        self.XS_table_w_Table_header()
        self.RE_LSCX_text.clear()
    #表头
    def XS_table_w_Table_header(self):
        try:
            _translate = QtCore.QCoreApplication.translate
            item = self.TH_table.horizontalHeaderItem(0)
            item.setText(_translate("MainWindow", "序号"))
            item = self.TH_table.horizontalHeaderItem(1)
            item.setText(_translate("MainWindow", "流水号"))
            item = self.TH_table.horizontalHeaderItem(2)
            item.setText(_translate("MainWindow", "条码"))
            item = self.TH_table.horizontalHeaderItem(3)
            item.setText(_translate("MainWindow", "名称"))
            item = self.TH_table.horizontalHeaderItem(4)
            item.setText(_translate("MainWindow", "规格"))
            item = self.TH_table.horizontalHeaderItem(5)
            item.setText(_translate("MainWindow", "数量"))
            item = self.TH_table.horizontalHeaderItem(6)
            item.setText(_translate("MainWindow", "单价"))
            item = self.TH_table.horizontalHeaderItem(7)
            item.setText(_translate("MainWindow", "折扣"))
            item = self.TH_table.horizontalHeaderItem(8)
            item.setText(_translate("MainWindow", "金额"))
        except AttributeError:
            pass


    #数据库操作方法
    def SJ_CZ_func(self):
        self.MYSQL_conn()
        for v in self.TH_dict.values():
            # 查询语句
            sql = "SELECT * FROM SP_List WHERE ID = '%s'" % v[1]
            # 提交命令
            self.cur.execute(sql)
            # 返回数据
            data = self.cur.fetchall()
            for i in data:
                kucun = int(i[4]) +1
                shuliang = int(i[5]) -1
                sql = """UPDATE SP_List SET sp_kucun = '%s' , sp_shouchu = '%s' WHERE ID = '%s'"""%(kucun,shuliang,v[1])

                self.cur.execute(sql)  # 像sql语句传递参数
                    # 提交
                self.conn.commit()
                #except Exception as e:
                    # 错误回滚
                 #   self.conn.rollback()
            sql = """DELETE FROM Sale_list WHERE Sale_id = '%s' AND Sp_id = '%s'"""%(v[0],v[1])
            try:
                self.cur.execute(sql)  # 像sql语句传递参数
                # 提交
                self.conn.commit()
            except Exception as e:
                # 错误回滚
                self.conn.rollback()
            sql = """insert into Return_list\
            (Sale_id,Sp_id,Sp_name,Sp_guige,Sp_leibie,Sp_danjia,Sp_shuliang,Sp_zhekou,Sp_zongjia,Operator,Salesman) \
            values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")"""\
                  % (v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8],self.mendian,self.Foreground_user )
            try:
                self.cur.execute(sql)  # 像sql语句传递参数
                # 提交
                self.conn.commit()
            except Exception as e:
                # 错误回滚
                self.conn.rollback()
        self.TH_dict.clear()
        self.DL_table_func()
        self.conn.close()
        self.TH_table.clearContents()


