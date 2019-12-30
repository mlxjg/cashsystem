from ui import inquireui
from PyQt5.QtWidgets import QMainWindow,QCompleter
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtGui import QRegExpValidator
from config import Config_set
class Inquire_system(QMainWindow,inquireui.Ui_MainWindow,Config_set):
    def __init__(self):
        super(Inquire_system, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("商品查询")
        self.Inquire_f()

    def Inquire_f(self):
        self.MYSQL_conn()
        # 设置补全列表
        Intelligent_input_list = []
        # 查询语句
        sql = """SELECT ID FROM SP_List"""
        # 提交命令
        self.cur.execute(sql)
        # 返回烽据
        data = self.cur.fetchall()
        # 遍历结果
        for x in data:
            Intelligent_input_list.append(x[0])
        self.conn.close()
        # 加载补全列表
        self.Ilist = QCompleter(Intelligent_input_list)
        # 增加自动补全
        self.SPselect_input.setCompleter(self.Ilist)
        # 设置匹配模式  有三种： Qt.MatchStartsWith 开头匹配（默认）  Qt.MatchContains 内容匹配  Qt.MatchEndsWith 结尾匹配
        self.Ilist.setFilterMode(QtCore.Qt.MatchContains)
        # 设置补全模式  有三种： QCompleter.PopupCompletion（默认）  QCompleter.InlineCompletion   QCompleter.UnfilteredPopupCompletion
        self.Ilist.setCompletionMode(QCompleter.PopupCompletion)
        # 给lineedit设置补全器
        self.SPselect_input.setCompleter(self.Ilist)
        # 给lineedit汪加回车确认
        self.SPselect_Button.clicked.connect(self.Input_table_xc)
        # 为Qlineedit添加正则，只允许输入数字
        Qreg = QtCore.QRegExp("[0-9\.]+$")
        ipValidator = QRegExpValidator(Qreg)
        self.SPselect_input.setValidator(ipValidator)
    #序列化MAP
    def Input_table_xc(self):
        self.MYSQL_conn()
        #获取用户输入内容
        user_input_id = self.SPselect_input.text()
        self.SPselect_input.clear()
        # 查询语句
        sql = "SELECT * FROM SP_List WHERE ID = '%s'" % user_input_id
        # 提交命令
        self.cur.execute(sql)
        # 返回数据
        data = self.cur.fetchall()
        _translate = QtCore.QCoreApplication.translate
        for i in data:
            item = QtWidgets.QTableWidgetItem()
            self.SPselect_table.setItem(0, 0, item)
            item.setText(_translate("MainWindow", i[0]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(12)
            item.setFont(font)
            item = QtWidgets.QTableWidgetItem()
            self.SPselect_table.setItem(0, 1, item)
            item.setText(_translate("MainWindow", i[1]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(12)
            item.setFont(font)
            item = QtWidgets.QTableWidgetItem()
            self.SPselect_table.setItem(0, 2, item)
            item.setText(_translate("MainWindow", i[2]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(12)
            item.setFont(font)
            item = QtWidgets.QTableWidgetItem()
            self.SPselect_table.setItem(0, 3, item)
            item.setText(_translate("MainWindow", i[3]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(12)
            item.setFont(font)
            item = QtWidgets.QTableWidgetItem()
            self.SPselect_table.setItem(0, 4, item)
            item.setText(_translate("MainWindow", i[4]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(12)
            item.setFont(font)
            item = QtWidgets.QTableWidgetItem()
            self.SPselect_table.setItem(0, 5, item)
            item.setText(_translate("MainWindow", i[5]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(12)
            item.setFont(font)
            item = QtWidgets.QTableWidgetItem()
            self.SPselect_table.setItem(0, 6, item)
            item.setText(_translate("MainWindow", i[7]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(12)
            item.setFont(font)

        self.conn.close()

