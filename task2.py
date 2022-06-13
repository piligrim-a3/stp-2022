import os
import ctypes
import requests
from PIL import Image
from datetime import datetime

pictureName = 'temp.png'

def getCurrentDate():
    return datetime.now().strftime("%Y %m %d")

def getScreenResolution():
    user32 = ctypes.windll.user32
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def getPictureURL(date):
    year, month, day = date.split()
    return 'https://anzu.sinc.ad.jp/himawari/img/D531106/thumbnail/550/{year}/{month}/{day}/042000_0_0.png'.\
        format(year=year, month=month, day=day)

def savePicture(url, fileName):
    response = requests.get(url)
    if response.ok:
        with open(fileName, 'wb') as f:
            f.write(response.content)
    else:
        raise Exception('Picture not found, try another day')

def setWallpaper(fileName):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(fileName), 0)


def transformPicture(fileName, sizes, fill_color=(0, 0, 0, 0)):
    im = Image.open(fileName)

    x, y = im.size
    x1, y1 = sizes

    new_im = Image.new('RGBA', (x1, y1), fill_color)
    new_im.paste(im, (int((x1 - x) / 2), int((y1 - y) / 2)))
    new_im.save(pictureName, 'PNG')

if __name__ == '__main__':
    url = getPictureURL(getCurrentDate())
    savePicture(url, pictureName)
    transformPicture(pictureName, getScreenResolution())
    setWallpaper(pictureName)


