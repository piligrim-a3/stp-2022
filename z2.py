import json
import requests
from bs4 import BeautifulSoup
from win32api import GetSystemMetrics
import fake_useragent


Width = GetSystemMetrics(0)
Height = GetSystemMetrics(1)
user = fake_useragent.UserAgent().random
header = {'user-agent': user}
linkDate = "https://ncthmwrwbtst.cr.chiba-u.ac.jp/img/FULL_24h/latest.json?_=1653998239673"
date = requests.post(linkDate, headers=header).text
date = json.loads(date)
print(date['date'])

print()
