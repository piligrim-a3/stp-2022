import json
import requests
from bs4 import BeautifulSoup
from win32api import GetSystemMetrics
import fake_useragent
from PIL import Image
import PIL.ImageOps


Width = GetSystemMetrics(0)
Height = GetSystemMetrics(1)
user = fake_useragent.UserAgent().random
header = {'user-agent': user}

linkDate = "https://ncthmwrwbtst.cr.chiba-u.ac.jp/img/FULL_24h/latest.json?_=1653998239673"
datetime = requests.post(linkDate, headers=header).text
date = json.loads(datetime)['date'].split()[0].split('-')
time = json.loads(datetime)['date'].split()[1].split(':')
print(date)
print(time)

linkIm = "https://anzu.sinc.ad.jp/himawari/img/FULL_24h/BlueMarble/1d/385/BlueMarble_0_0.png"
img_data = requests.get(linkIm).content
with open('earth.png', 'wb') as handler:
    handler.write(img_data)

linkIm = "https://anzu.sinc.ad.jp/himawari/img/FULL_24h/B13/1d/550/" + date[0] + "/" + date[1] + "/" + date[2] + "/" + ''.join(time) + "_0_0.png"
img_data = requests.get(linkIm).content
with open('cloud.png', 'wb') as handler:
    handler.write(img_data)

img_earth = Image.open('earth.png').convert('RGBA')
img_cloud = Image.open('cloud.png').convert('RGBA')
width, height = img_earth.size
img_cloud = img_cloud.resize((width, height))
img_cloud.save('cloud.png')
img_earth.paste(img_cloud, (0, 0), img_cloud)
img_earth.save('result.png', quality=100)


# im = Image.open(name_open)
# result = Image.new('RGB', im.size)
# x, y = im.size
# r, g, b = im.getpixel((i, j))
# result.putpixel((i, j), (nr, ng, nb))
# new_im = result.transpose(Image.FLIP_LEFT_RIGHT)