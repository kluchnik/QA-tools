#!/usr/bin/python3

import subprocess as sp

from datetime import datetime
import sys

url = sys.argv[1]
width = sys.argv[2]
height = sys.argv[3]
timeout = sys.argv[4]
directory = sys.argv[5]

print ('URL адрес: ' + url)
print ('Разрешение экрана: ' + width + 'x' + height)
print ('Ожидание загрузки страницы: ' + timeout + ' сек')
print ('Директория для сохранения страниц: ' + directory)

print ('\x1b[1;32;40m' + datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + ' скрипт запущен: ' + '\x1b[0m')

time = datetime.strftime(datetime.now(), "%Y.%m.%d-%H:%M:%S")
filename ='/home/script-server/conf/' + str(directory)[3:]  + '/' + time + '.png'
status,result = sp.getstatusoutput('wkhtmltoimage' + ' --javascript-delay ' + timeout + '000' + ' --width ' + width + ' --height ' + height + ' ' + url + ' ' + filename)
print ('Файл сохранен: http://192.168.1.2:8080/file/' + str(directory)[3:]  + '/' + time + '.png') if status==0 else ('Ошибка сохранения')

print ('\x1b[1;32;40m' + datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + ' скрипт завершен' + '\x1b[0m')
