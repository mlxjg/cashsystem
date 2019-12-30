from ui import loginui
from cash import Cash
from config import Config_set
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
import sys

class Login_user(QMainWindow,loginui.Ui_MainWindow,Config_set):
    def __init__(self,):
        super(Login_user, self).__init__()
        self.setupUi(self)
        self.Windows_title_set_func()
        self.User_table_py = {}
        self.Passwd_line.returnPressed.connect(self.Check_user)
        self.Login_button.clicked.connect(self.Check_user)
        self.show()
    def Check_user(self):
        self.MYSQL_conn()
        user_text = self.User_line.text()
        user_passwd = self.Passwd_line.text()
        sql = """SELECT User_name,User_passwd FROM User_table """
        # 提交命令
        self.cur.execute(sql)
        # 返回数据
        data = self.cur.fetchall()
        for i,v in data:
            if user_text == i:
                if user_passwd == v:
                    self.Cash =Cash(i)
                    self.Cash.show()
                    self.close()
        self.cur.close()

if __name__ == "__main__":
    app =  QApplication(sys.argv)
    try:
        win = Login_user()
        win.show()
    except AttributeError:
        print("key")
    except ValueError:
        print("key")

    sys.exit(app.exec_())
