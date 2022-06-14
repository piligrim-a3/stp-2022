import requests
import ctypes
import os

link = "http://k2go.jp/public/ImageViewer/sample/img/sample.png"
#запрос на получение изображения планеты
planet = requests.get(link).content
#сохранение изображения из запроса
with open('planet.jpg', 'wb') as handler:
    handler.write(planet)
#установка изображения на рабочий стол из папки с проектом
ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath('planet.jpg'), 0)
