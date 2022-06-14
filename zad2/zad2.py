import urllib.request
import struct
import ctypes
import os
import datetime

#определение текущей даты
date = datetime.datetime.today()

#парсим изображение
imgURL = "https://ncthmwrwbtst.cr.chiba-u.ac.jp/img/D531106/thumbnail/550/"+date.strftime('%Y')+"/"+date.strftime('%m')+"/"+date.strftime('%d')+"/090000_0_0.png"
print(imgURL)

#путь целевого изображения где мы его сохраняем
put = "C:/Users/"+os.environ.get( "USERNAME" )+"/Desktop/123.jpg"
urllib.request.urlretrieve(imgURL, put)

print(put)
PATH = put
#PATH = 'C:\\image.jpg'

#Установка рисунка для обоев Рабочего стола. uiParam должна быть установлена в 0. pvParam- Строка,содержащая имя файла рисунка, чтобы использовать как обои
SPI_SETDESKWALLPAPER = 20

#проверка на разрядность системы
def is_64bit_windows():
    """Check if 64 bit Windows OS"""
    return struct.calcsize('P') * 8 == 64

#функция смены фона на целевое изображение
def changeBG(path):
    """Change background depending on bit size"""
    #в зависимости от разрядности системы разные конфигурации
    if is_64bit_windows():
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, PATH, 3)
    else:
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, PATH, 3)

#меняем обои
changeBG(PATH)

