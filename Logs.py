import zipfile
import sqlite3
import os

#разархивирование архива access.zip
archive = 'access.zip'
with zipfile.ZipFile(archive, 'r') as zip_file:
    zip_file.extractall("extract")

#открытие распакованого файла с логами access.log
f = open("extract/access.log")
#назначение текстовой переменной текстового содержимого с файла access.log
data = f.read()

#замена в переменной data одного текста на другой
#data.replace('-', '')
data = data.replace('-', '')
data = data.replace('    ', ' ')
data = data.replace('  ', ' ')
data = data.replace('  ', ' ')
data = data.replace('  ', ' ')
data = data.replace('\n', ' ')
#разделяем строковую переменную на массив. Разделителем является пробел
data = data.split(" ")

#создаем базу logi.db и конектимся к ней, а так же таблицу с названием spisok
conn = sqlite3.connect('logi.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS spisok(
      time TEXT,
      elapsed TEXT,
      remotehost TEXT,
      code_status TEXT,
      bytes INT,
      method TEXT,
      URL TEXT,
      peerstatus_peerhost TEXT,
      type TEXT);
   """)
conn.commit()