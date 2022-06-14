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