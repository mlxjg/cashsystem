from ui import cashui
from PyQt5.QtWidgets import QMainWindow,QCompleter,QMenu,QMessageBox
from PyQt5 import QtCore,QtWidgets,QtGui
import datetime,random
from bin.inquire import Inquire_system
from bin.statistics import Statisticsui_system
from bin.returnback import Returnback_system
from bin.expend import Expend_system
from config import Config_set

from admin.adminman import Admin_main

class Cash(QMainWindow,cashui.Ui_MainWindow,Config_set):
    def __init__(self,Foreground_user):
        super(Cash, self).__init__()
        self.setupUi(self)
        self.Windows_title_set_func()
        self.Mendian()
        #设置表格尺寸
        self.SJ_view.setColumnWidth(1, 400)
        self.SJ_view.setColumnWidth(0, 300)
        self.Foreground_user = Foreground_user
        self.Syy_text.setText(self.Foreground_user)
        self.Select_button.clicked.connect(self.CX_func)
        self.Census_button.clicked.connect(self.Census_func)
        self.Back_button.clicked.connect(self.Th_button_func)
        self.ZC_button.clicked.connect(self.ZC_button_func)
        self.Backstage_button.clicked.connect(self.Backstage_func)
        self.gwc_map = {}
        self.js_map = {}
        self.SPID = self.Shop_id()
        self.User_input()
        self.JS_button.clicked.connect(self.Js_button)
        # 设置右击菜单
        self.SJ_view.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.SJ_view.customContextMenuRequested.connect(self.showContextMenu)
        self.Zk_text.returnPressed.connect(self.Zk_function)
        self.SF_view.returnPressed.connect(self.Sf_function)

        self.show()
    #实现用户输入的提示列表
    def User_input(self):
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
        self.xlist = QCompleter(Intelligent_input_list)
        # 增加自动补全
        self.CX_text.setCompleter(self.xlist)
        # 设置匹配模式  有三种： Qt.MatchStartsWith 开头匹配（默认）  Qt.MatchContains 内容匹配  Qt.MatchEndsWith 结尾匹配
        self.xlist.setFilterMode(QtCore.Qt.MatchContains)
        # 设置补全模式  有三种： QCompleter.PopupCompletion（默认）  QCompleter.InlineCompletion   QCompleter.UnfilteredPopupCompletion
        self.xlist.setCompletionMode(QCompleter.PopupCompletion)
        # 给lineedit设置补全器
        self.CX_text.setCompleter(self.xlist)
        # 给lineedit汪加回车确认
        self.CX_text.returnPressed.connect(self.Serializemap)
        # 为Qlineedit添加正则，只允许输入数字
        Qreg = QtCore.QRegExp("[0-9\.]+$")
        ipValidator = QtGui.QRegExpValidator(Qreg)
        self.Zk_text.setValidator(ipValidator)
        self.SF_view.setValidator(ipValidator)

    #序列化MAP
    def Serializemap(self):
        self.MYSQL_conn()
        #获取用户输入内容
        user_input_id = self.CX_text.text()
        # 查询语句
        sql = "SELECT * FROM SP_List WHERE ID = '%s'" % user_input_id
        # 提交命令
        self.cur.execute(sql)
        # 返回数据
        data = self.cur.fetchall()
        # 遍历结果
        zk_num = 100
        sl_num = 1
        LS_num = self.LS_view.text()
        for x in data:
            self.gwc_map[x[0]] = [LS_num,x[1],x[7],str(zk_num), str(sl_num),str(int(zk_num*0.01)*sl_num*x[7]),x[8],x[2],x[3]]
        self.conn.close()
        self.Maptolist()
    #生成购物ID
    def Shop_id(self):
        for i in range(0, 10):
            nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  # 生成当前时间
            randomNum = random.randint(100, 999)  # 生成的随机整数n，其中0<=n<=100
            uniqueNum = str(nowTime) + str(randomNum)
            self.LS_view.setText(uniqueNum)
            return uniqueNum
    #生成前端显示购物车清单
    def Maptolist(self):
        self.buchang = 0
        if self.buchang < 15:
            for k, v in self.gwc_map.items():
                _translate = QtCore.QCoreApplication.translate
                item = QtWidgets.QTableWidgetItem()
                self.SJ_view.setItem(self.buchang, 0, item)
                item.setText(_translate("MainWindow", k))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                font = QtGui.QFont()
                font.setPointSize(12)
                item.setFont(font)

                item = QtWidgets.QTableWidgetItem()
                self.SJ_view.setItem(self.buchang, 1, item)
                item.setText(_translate("MainWindow", v[1]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                font = QtGui.QFont()
                font.setPointSize(12)
                item.setFont(font)

                item = QtWidgets.QTableWidgetItem()
                self.SJ_view.setItem(self.buchang, 2, item)
                item.setText(_translate("MainWindow", v[2]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                font = QtGui.QFont()
                font.setPointSize(12)
                item.setFont(font)
                f = float(v[3])
                f ="%.0f" % f
                item = QtWidgets.QTableWidgetItem()
                self.SJ_view.setItem(self.buchang, 3, item)
                item.setText(_translate("MainWindow", str(f)))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                font = QtGui.QFont()
                font.setPointSize(12)
                item.setFont(font)
                item = QtWidgets.QTableWidgetItem()
                self.SJ_view.setItem(self.buchang, 4, item)
                item.setText(_translate("MainWindow", v[4]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                font = QtGui.QFont()
                font.setPointSize(12)
                item.setFont(font)
                item = QtWidgets.QTableWidgetItem()
                self.SJ_view.setItem(self.buchang, 5, item)
                item.setText(_translate("MainWindow", v[5]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                font = QtGui.QFont()
                font.setPointSize(12)
                item.setFont(font)
                self.buchang = self.buchang + 1
            else:
                pass
        self.View_sl()

    def showContextMenu(self, pos):

        # 计算有多少条数据，默认-1,
        row_num = -1
        for i in self.SJ_view.selectionModel().selection().indexes():
            row_num = i.row()
        # 表格中只有两条有效数据，所以只在前两行支持右键弹出菜单
        if row_num < 16:
            menu = QMenu()
            item1 = menu.addAction(u'删除')
            action = menu.exec_(self.SJ_view.mapToGlobal(pos))
            #设置删除内容行
            try:
                if action == item1:
                    row_select = self.SJ_view.selectedItems()
                    id = row_select[0].text()
                    row = row_select[0].text()
                    del self.gwc_map[id]
                    #清除表格内容
                    self.SJ_view.clearContents()
                    self.Maptolist()
                else :
                    pass
            except KeyError:
                pass

    #实现数量及应该收方法
    def View_sl(self):
        data = 0
        f = 0
        for v in self.gwc_map.values():
            data = int(data + float(v[4]))
            h = 0 + (float(v[2]))*(float(v[3])/100)*(float(v[4]))
            f = f + h
        self.SL_view.setText(str(data))
        self.YS_view.setText(str("%.0f"% f))

    #折扣区块
    def Zk_function(self):
        zk_data = self.Zk_text.text()
        for k,v in self.gwc_map.items():
            self.gwc_map[k][3] = zk_data
            f = float(v[3]) / 100 * float(v[2]) * float(v[4])
            self.gwc_map[k][5] = str("%.0f"% f)
        self.Zk_text.setText("")
        self.SF_view.clear()
        self.Maptolist()

    # 实付区块
    def Sf_function(self):
        sum_h = 0
        for k,v in self.gwc_map.items():

            self.gwc_map[k][3] = "100"
            sumhe = self.gwc_map[k][5] = 1 * float(v[2]) * float(v[4])
            sum_h = sumhe + sum_h
        sf_data = int(self.SF_view.text())
        yf_data = int(self.YS_view.text())

        if sf_data != 0 and yf_data != 0:
            f = sf_data / sum_h * 100
            data = "%.2f"% f
            for k,v in self.gwc_map.items():
                self.gwc_map[k][3] = data
                f = float(v[3]) / 100 * float(v[2]) * float(v[4])
                self.gwc_map[k][5] = str("%.0f" % f)
            self.SF_view.clear()
            self.Maptolist()
    #查询方法
    def CX_func(self):
        self.Inquire_system = Inquire_system()
        self.Inquire_system.show()
    #统计方法
    def Census_func(self):
        self.Statisticsui_system = Statisticsui_system(self.Foreground_user)
        self.Statisticsui_system.show()
    #后台方法
    def Backstage_func(self):
        self.MYSQL_conn()
        # 设置补全列表
        Intelligent_input_list = []
        # 查询语句
        sql = """SELECT User_level FROM User_table WHERE User_name = '%s'""" % self.Foreground_user
        # 提交命令
        self.cur.execute(sql)
        # 返回烽据
        data = self.cur.fetchall()
        if data[0][0] == "A":
            self.admin_main = Admin_main()
            self.admin_main.show()
        elif data[0][0] == "B":
            QMessageBox.about(self,"权限错误","您非管理员，无权访问！")
    def Th_button_func(self):
        self.Returnback_system = Returnback_system(self.Foreground_user)
        self.Returnback_system.show()
    def ZC_button_func(self):
        self.Expend_system = Expend_system()
        self.Expend_system.show()
    def Js_button(self):
        self.MYSQL_conn()
        for k, v in self.gwc_map.items():
            sql = "SELECT sp_jinjia,sp_kucun,sp_shouchu FROM SP_List WHERE ID = '%s'" % k
            self.cur.execute(sql)
            data = self.cur.fetchall()
            for i in data:
                a = int(i[1])-1
                b = int(i[2])+1
                self.js_map[k] = [i[0],a,b]
        for k,v in self.js_map.items():
            sql = """update SP_List set sp_kucun = '%s'  where ID = '%s'  """
            try:
                self.cur.execute(sql % (v[1],k))  # 像sql语句传递参数
                # 提交
                self.conn.commit()
            except Exception as e:
                # 错误回滚
                self.conn.rollback()

            sql = """update SP_List set sp_shouchu = '%s'  where ID = '%s'  """
            try:
                self.cur.execute(sql % (v[2],k))  # 像sql语句传递参数
                # 提交
                self.conn.commit()
            except Exception as e:
                # 错误回滚
                self.conn.rollback()
        for k,v in self.gwc_map.items():
            sql = """insert into Sale_list(Sale_id,Sp_id,Sp_name,Sp_danjia,Sp_shuliang,Sp_zhekou,\
                Sp_zongjia,Sp_jinjia,Operator,Salesman,Sp_leibie,Sp_guige) values\
                ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")"""\
                  % (v[0],k,v[1],v[2],v[4],v[3],v[5],v[6],self.mendian,self.Foreground_user,v[8],v[7])
            try:
                self.cur.execute(sql)  # 像sql语句传递参数
                # 提交
                self.conn.commit()
            except Exception as e:
                # 错误回滚
                self.conn.rollback()
        self.conn.close()
        self.js_map.clear()
        self.gwc_map.clear()
        self.SJ_view.clearContents()
        self.CX_text.clear()
        self.Shop_id()
        self.Maptolist()






