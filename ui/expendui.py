# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expendui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(989, 163)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ZC_date = QtWidgets.QDateEdit(self.centralwidget)
        self.ZC_date.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ZC_date.setFont(font)
        self.ZC_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 9, 1), QtCore.QTime(0, 0, 0)))
        self.ZC_date.setCalendarPopup(True)
        self.ZC_date.setObjectName("ZC_date")
        self.horizontalLayout.addWidget(self.ZC_date)
        self.ZC_cash = QtWidgets.QLineEdit(self.centralwidget)
        self.ZC_cash.setMinimumSize(QtCore.QSize(140, 30))
        self.ZC_cash.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ZC_cash.setFont(font)
        self.ZC_cash.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ZC_cash.setAlignment(QtCore.Qt.AlignCenter)
        self.ZC_cash.setObjectName("ZC_cash")
        self.horizontalLayout.addWidget(self.ZC_cash)
        self.ZC_leibie = QtWidgets.QComboBox(self.centralwidget)
        self.ZC_leibie.setMinimumSize(QtCore.QSize(190, 30))
        self.ZC_leibie.setMaximumSize(QtCore.QSize(190, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ZC_leibie.setFont(font)
        self.ZC_leibie.setObjectName("ZC_leibie")
        self.ZC_leibie.addItem("")
        self.ZC_leibie.addItem("")
        self.ZC_leibie.addItem("")
        self.ZC_leibie.addItem("")
        self.ZC_leibie.addItem("")
        self.horizontalLayout.addWidget(self.ZC_leibie)
        self.ZC_beizhu = QtWidgets.QLineEdit(self.centralwidget)
        self.ZC_beizhu.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ZC_beizhu.setFont(font)
        self.ZC_beizhu.setObjectName("ZC_beizhu")
        self.horizontalLayout.addWidget(self.ZC_beizhu)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.ZC_TJ_button = QtWidgets.QPushButton(self.centralwidget)
        self.ZC_TJ_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ZC_TJ_button.setFont(font)
        self.ZC_TJ_button.setObjectName("ZC_TJ_button")
        self.verticalLayout.addWidget(self.ZC_TJ_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "支出"))
        self.label.setText(_translate("MainWindow", "     日期           金额          类别                           备注"))
        self.ZC_leibie.setItemText(0, _translate("MainWindow", "服装采购"))
        self.ZC_leibie.setItemText(1, _translate("MainWindow", "店面差旅"))
        self.ZC_leibie.setItemText(2, _translate("MainWindow", "快递费"))
        self.ZC_leibie.setItemText(3, _translate("MainWindow", "日常物品采购"))
        self.ZC_leibie.setItemText(4, _translate("MainWindow", "其它"))
        self.ZC_TJ_button.setText(_translate("MainWindow", "提交"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
