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