import json
import requests
import fake_useragent
import qrcode

session = requests.Session()
user = fake_useragent.UserAgent().random
header = {'user-agent': user}
link = "https://bgpu.ru/campus/api/v1/auth"
data = {'login': '1558',
        'pwd': 'n6hgur'}
authorization = session.post(link, data=data, headers=header)
link = "https://lk.bgpu.ru/campus/api/v1/area/qr?index=1"
indexes = session.get(link, headers=header).text
data = json.loads(indexes)
