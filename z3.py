import sys
import json
import requests
import fake_useragent
import qrcode
from PyQt6 import uic, QtWidgets
from form import Ui_Dialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel, QFileDialog
from PyQt6 import QtGui
import os


#lgn: 1558
#pwd: n6hgur
session = requests.Session()
user = fake_useragent.UserAgent().random
header = {'user-agent': user}
Form, Window = uic.loadUiType("form.ui")
valid_id = 0


def login(lgn, pwd):
        link = "https://bgpu.ru/campus/api/v1/auth"
        data = {'login': lgn,
                'pwd': pwd}
        return session.post(link, data=data, headers=header)


def new_qr():
        link = "https://lk.bgpu.ru/campus/api/v1/area/qr?index=" + str(valid_id + 1)
        indexes = session.get(link, headers=header).text
        return json.loads(indexes)


def counter_index():
        actual_code_link = "https://lk.bgpu.ru/campus/api/v1/area/counter-index"
        code = session.get(actual_code_link, headers=header).text
        return json.loads(code)


def create_qr(jqr):
        global valid_id
        img = qrcode.make(jqr[0]['qr'])
        img.save("qr.png")
        # print(*jqr, sep='\n')
        valid_id = jqr[0]['countIndex']
        return "qr.png"


class Ui(QtWidgets.QDialog, Form):
        def __init__(self):
                super(Ui, self).__init__()
                self.ui = Ui_Dialog()
                self.ui.setupUi(self)
                self.initUI()

        def buttonPresed(self):
                lgn = self.ui.lineEdit.text()
                pwd = self.ui.lineEdit_2.text()
                p = login(lgn, pwd)
                if '<Response [200]>' == str(p):
                        self.ui.lineEdit.setText('')
                        self.ui.lineEdit_2.setText('')
                        url = os.path.abspath(create_qr(new_qr()))
                        img = QPixmap(url)
                        self.ui.label_3.setPixmap(img)
                        self.visible_ui()

        def buttonPresed_3(self):
                url = os.path.abspath(create_qr(new_qr()))
                img = QPixmap(url)
                self.ui.label_3.setPixmap(img)

        def buttonPresed_4(self):
                p = counter_index()
                self.ui.label_4.setText(str(p))

        def buttonPresed_2(self):
                self.visible_ui()

        def initUI(self):
                self.ui.pushButton.clicked.connect(self.buttonPresed)
                self.ui.pushButton_2.clicked.connect(self.buttonPresed_2)
                self.ui.pushButton_3.clicked.connect(self.buttonPresed_3)
                self.ui.pushButton_4.clicked.connect(self.buttonPresed_4)
                self.ui.lineEdit.setText('1558')
                self.ui.lineEdit_2.setText('n6hgur')
                lgn = self.ui.lineEdit.text()
                pwd = self.ui.lineEdit_2.text()
                login(lgn, pwd)
                self.ui.label_3.setVisible(self.ui.label_3.isVisible())
                self.ui.pushButton_2.setVisible(self.ui.pushButton_2.isVisible())
                self.ui.label_4.setVisible(self.ui.label_4.isVisible())
                self.ui.pushButton_4.setVisible(self.ui.pushButton_4.isVisible())

        def visible_ui(self):
                self.ui.lineEdit.setVisible(not self.ui.lineEdit.isVisible())
                self.ui.lineEdit_2.setVisible(not self.ui.lineEdit_2.isVisible())
                self.ui.pushButton.setVisible(not self.ui.pushButton.isVisible())
                self.ui.label.setVisible(not self.ui.label.isVisible())
                self.ui.label_2.setVisible(not self.ui.label_2.isVisible())
                self.ui.label_3.setVisible(not self.ui.label_3.isVisible())
                self.ui.pushButton_2.setVisible(not self.ui.pushButton_2.isVisible())
                self.ui.label_4.setVisible(not self.ui.label_4.isVisible())
                self.ui.pushButton_4.setVisible(not self.ui.pushButton_4.isVisible())


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        w = Ui()
        w.show()
        sys.exit(app.exec())