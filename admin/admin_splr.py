from ui.adminui import Ui_MainWindow
from PyQt5.QtWidgets import QWidget,QMessageBox
from PyQt5.QtPrintSupport import QPrinter, QPrinterInfo
from PyQt5.QtGui import QTextDocument
from PyQt5.QtCore import QSizeF
import datetime,random
import barcode
from barcode.writer import ImageWriter
from os import environ
class Spgl(QWidget,Ui_MainWindow):
    def __init__(self):
        super(Spgl, self).__init__()
        self.setupUi(self)
        self.TEMP_barcode = ""
    def Spgl_sprk_button(self):
        self.Spgl_tj_button.clicked.connect(self.Text_Obtain)
        self.Spgl_splr_random.clicked.connect(self.Shop_id)
        self.Spgl_splr_bqsc.clicked.connect(self.Bqyl_func)
        self.Spgl_splr_print.clicked.connect(self.Bqdy_func)

    def Text_Obtain(self):
        self.spgl_sptm = self.Spgl_sptm.text()
        self.spgl_spmc = self.Spgl_spmc.text()
        self.spgl_spgg = self.Spgl_spgg.text()
        self.spgl_splb = self.Spgl_splb.text()
        self.spgl_spsl = self.Spgl_spsl.text()
        self.spgl_spdw = self.Spgl_spdw.text()
        self.spgl_spjj = self.Spgl_spjj.text()
        self.spgl_sphyj = self.Spgl_sphyj.text()
        self.spgl_splsj = self.Spgl_splsj.text()
        self.spgl_spghs = self.Spgl_spghs.text()
        if len(self.spgl_sptm) != 0 and len(self.spgl_spmc) != 0 and len(self.spgl_spgg) != 0 and len(self.spgl_splb) != 0 \
                and len(self.spgl_spsl) != 0 and len(self.spgl_spdw) != 0  and len(self.spgl_spjj) != 0 and len(self.spgl_sphyj) != 0 \
                and len(self.spgl_splsj) != 0:
                self.MYSQL_conn()
                sql = """insert into SP_List\
                (ID,SP_name,sp_guige,sp_leibie,sp_kucun,sp_danwei,sp_lingshou,sp_jinjia,sp_gys,sp_shouchu) \
                values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")""" \
                      % (self.spgl_sptm,self.spgl_spmc,self.spgl_spgg,self.spgl_splb,self.spgl_spsl,self.spgl_spdw,self.spgl_splsj,self.spgl_spjj,self.spgl_spghs,"0")
                try:
                    self.cur.execute(sql)  # 像sql语句传递参数
                    # 提交
                    self.conn.commit()
                except Exception as e:
                    # 错误回滚
                    self.conn.rollback()
                self.conn.close()
                self.Spgl_sptm.clear()
                self.Spgl_spmc.clear()
                self.Spgl_spgg.clear()
                self.Spgl_splb.clear()
                self.Spgl_spsl.clear()
                self.Spgl_spjj.clear()
                self.Spgl_sphyj.clear()
                self.Spgl_splsj.clear()
                self.Spgl_spghs.clear()
        else:
            QMessageBox.about(self, "输入有误", "输入内容不能为空！")
    def Shop_id(self):
        xjg =""
        for i in range(0, 10):
            nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  # 生成当前时间
            randomNum = random.randint(100, 999)  # 生成的随机整数n，其中0<=n<=100
            uniqueNum = str(nowTime) + str(randomNum)
            xjg = uniqueNum
            self.Spgl_sptm.setText(uniqueNum)
            # 获取系统TEMP路径
        self.TEMP_barcode = r"%s\%s"%(environ.get("TMP"),xjg)
        Code = barcode.get_barcode_class('code128')  # 参数为支持的格式
        # 获取条形码对象
        bar = Code(xjg,writer=ImageWriter())
        bar.save(self.TEMP_barcode,{'module_width': 0.4, 'module_height': 13.0, 'font_size': 25, 'text_distance': 0.5})

    #生成标签预缆方法
    def Bqyl_func(self):
        sptm = self.Spgl_sptm.text()
        zh_name = self.Spgl_splr_zh_name.text()
        zh_cash = self.Spgl_splr_zh_cash.text()
        tm_width = self.Spgl_splr_tm_width.text()
        tm_height = self.Spgl_splr_tm_height.text()
        spmc = self.Spgl_spmc.text()
        spgg = self.Spgl_spgg.text()
        mc = spmc+"-"+spgg
        splsj = self.Spgl_splsj.text()
        # 获取编码类

        html = """
        <head>
        <title>Report</title>
        </head>
        <body>
        <tr>
        <td><h1><font size="{}">{}</font></h1></td>
        </tr>
        <tr>
        <td><h1><font size="{}">价格：{}</font></h1></td>
        </tr>
        <p align=lift><img src="{}"" width="{}" height="{}"></p>
        </body>
        """.format(zh_name,mc,zh_cash,splsj,self.TEMP_barcode+".png",tm_width,tm_height)
        self.Spgl_splr_ylxg.setHtml(html)
    #实现标签打印功能
    def Bqdy_func(self):
        html1 = self.Spgl_splr_ylxg.toHtml()
        p = QPrinterInfo.defaultPrinter()  # 获取默认打印机
        print_device = QPrinter(p)
        document = QTextDocument()
        lift_margin = self.Spgl_splr_pagelift_margin.text()
        right_margin = self.Spgl_splr_pageright_margin.text()
        print_device.setPageMargins(float(lift_margin), float(right_margin), 0, 0, QPrinter.Millimeter)
        document.setPageSize(QSizeF(print_device.pageRect().size()))
        document.setHtml(html1)
        #实现按数量打印标签
        SPSL = self.Spgl_spsl.text()
        a = 1
        while a<=int(SPSL):
            document.print(print_device)
            a = a+1
        self.Spgl_splr_ylxg.clear()