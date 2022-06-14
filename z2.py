import json
import requests
from win32api import GetSystemMetrics
import fake_useragent
from PIL import Image
import ctypes
import os

'''Текущая высота и ширина монитора'''
Width = GetSystemMetrics(0)
Height = GetSystemMetrics(1)
'''подставной юзераген для запросов'''
user = fake_useragent.UserAgent().random
header = {'user-agent': user}

'''Отправляем первый запрос который возращает текущую дату'''
linkDate = "https://ncthmwrwbtst.cr.chiba-u.ac.jp/img/FULL_24h/latest.json?_=1653998239673"
datetime = requests.post(linkDate, headers=header).text
date = json.loads(datetime)['date'].split()[0].split('-')
time = json.loads(datetime)['date'].split()[1].split(':')

'''Второй запрос который возвращает планету без метеоданных'''
linkIm = "https://anzu.sinc.ad.jp/himawari/img/FULL_24h/BlueMarble/1d/770/BlueMarble_0_0.png"
img_data = requests.get(linkIm).content
with open('earth.png', 'wb') as handler:
    handler.write(img_data)

'''Третий запрос который возвращает метеоданные'''
linkIm = "https://anzu.sinc.ad.jp/himawari/img/FULL_24h/B13/1d/550/" + date[0] + "/" + date[1] + "/" + date[2] + "/" + ''.join(time) + "_0_0.png"
img_data = requests.get(linkIm).content
with open('cloud.png', 'wb') as handler:
    handler.write(img_data)

'''Соединяем два изображения, планету и метеоданные'''
img_earth = Image.open('earth.png').convert('RGBA')
widthE, heightE = img_earth.size
img_cloud = Image.open('cloud.png').convert('RGBA').resize((widthE, heightE))
img_cloud.save('cloud.png')
img_earth.paste(img_cloud, (0, 0), img_cloud)

'''устанавливаем изображение на рабочий стол'''
x, y = img_earth.size
img_earth = img_earth.resize((int(x * (Height / y)), Height))
img_earth.save('result.png', quality=100)
ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath('result.png'), 0)