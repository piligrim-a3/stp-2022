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