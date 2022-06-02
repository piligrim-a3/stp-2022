import json
import requests
import fake_useragent
import qrcode
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow

import sys

#lgn: 1558
#pwd: n6hgur
session = requests.Session()
user = fake_useragent.UserAgent().random
header = {'user-agent': user}


def login(lgn, pwd):
        link = "https://bgpu.ru/campus/api/v1/auth"
        data = {'login': lgn,
                'pwd': pwd}
        session.post(link, data=data, headers=header)


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
        print(jqr[-1]['qr'])
        type(img)
        img.save("qr.png")