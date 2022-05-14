import webbrowser
import pyautogui
import time
import ctypes
import pathlib
from PIL import ImageGrab, ImageTk

fileName = 'picture.png'
# Открываем сайт и браузер
webbrowser.open('http://k2go.jp/himawari/realtime/demo-mode/')
# Ждём пока загрузиться сайт
time.sleep(10)
# Делаем скриншот
pyautogui.press('printscreen')

im = ImageGrab.grabclipboard()
im.save(fileName,'PNG')

time.sleep(5)
SPI_SETDESKWALLPAPER = 20
path = str(pathlib.Path().resolve()) + '\\' + fileName
ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)