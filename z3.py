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


def login(lgn, pwd):
        link = "https://bgpu.ru/campus/api/v1/auth"
        data = {'login': lgn,
                'pwd': pwd}
        return session.post(link, data=data, headers=header)


def new_qr():
        link = "https://lk.bgpu.ru/campus/api/v1/area/qr?index=1"
        indexes = session.get(link, headers=header).text
        return json.loads(indexes)


def valid_qr(jqr):
        print(*jqr, sep='\n')
        actual_code_link = "https://lk.bgpu.ru/campus/api/v1/area/counter-index"
        code = session.get(actual_code_link, headers=header).text
        return json.loads(code)


def create_qr(jqr):
        img = qrcode.make(jqr[-1]['qr'])
        img.save("qr.png")
        return "qr.png"


class Ui(QtWidgets.QDialog, Form):
        def __init__(self):
                super(Ui, self).__init__()
                self.ui = Ui_Dialog()
                self.ui.setupUi(self)
                self.ui.pushButton.clicked.connect(self.buttonPresed)
                self.ui.lineEdit.setText('1558')
                self.ui.lineEdit_2.setText('n6hgur')
                self.initUI()

        def buttonPresed(self):
                lgn = self.ui.lineEdit.text()
                pwd = self.ui.lineEdit_2.text()
                p = login(lgn, pwd)
                if '<Response [200]>' == str(p):
                        url = os.path.abspath(create_qr(new_qr()))
                        pixmap = QPixmap(url)
                        label = QLabel(self.ui.label_3)
                        label.setPixmap(pixmap)


        def initUI(self):
                lgn = self.ui.lineEdit.text()
                pwd = self.ui.lineEdit_2.text()
                login(lgn, pwd)
                label = QLabel(self.ui.label_3)
                pixmap = QPixmap(os.path.abspath(create_qr(new_qr())))
                label.setPixmap(pixmap)
                self.show()

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        w = Ui()
        w.show()
        sys.exit(app.exec())