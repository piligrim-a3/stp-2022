import json
import requests
from bs4 import BeautifulSoup
from win32api import GetSystemMetrics
import fake_useragent
from PIL import Image


Width = GetSystemMetrics(0)
Height = GetSystemMetrics(1)
user = fake_useragent.UserAgent().random
header = {'user-agent': user}

linkDate = "https://ncthmwrwbtst.cr.chiba-u.ac.jp/img/FULL_24h/latest.json?_=1653998239673"
date = requests.post(linkDate, headers=header).text
date = json.loads(date)
print(date['date'])

linkIm = "https://anzu.sinc.ad.jp/himawari/img/FULL_24h/BlueMarble/1d/385/BlueMarble_0_0.png"
img_data = requests.get(linkIm).content
with open('wallpaper.jpg', 'wb') as handler:
    handler.write(img_data)




# im = Image.open(name_open)
# result = Image.new('RGB', im.size)
# x, y = im.size
# r, g, b = im.getpixel((i, j))
# result.putpixel((i, j), (nr, ng, nb))
# new_im = result.transpose(Image.FLIP_LEFT_RIGHT)