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

#переменная счетчик
i = 0

#заполняем базу данных. каждая строка в файле логов - 1 строка в базе данных
while(i<len(data)):
    cur.execute(
        "INSERT INTO spisok (time, elapsed, remotehost, code_status, bytes, method, URL, peerstatus_peerhost, type) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (data[i], data[i+1], data[i+2], data[i+3], data[i+4], data[i+5],
         data[i+6], data[i+7], data[i+8]))
    conn.commit()
    #плюсуем к счетчику единицу
    i = i + 9


conn = sqlite3.connect('logi.db')
cur = conn.cursor()

#выполняем запрос в базу с сортировкой значений по убыванию по столбцу bytes (величина трафика)
itog_vivod = cur.execute("SELECT * FROM spisok ORDER BY bytes DESC limit 10").fetchall()

#заполняем текстовую переменную 10 строками со значениями с логов. С наибольшим трафиком
vivod_text = ""
for row in itog_vivod:
    vivod_text = vivod_text  + "%s %s %s %s %s %s %s %s %s"%(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]) + "\n"

#заполнение файла out.txt полученными данными
with open("extract/out.txt", "w") as file:
    file.write(vivod_text)
