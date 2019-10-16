#!/usr/bin/python3

# Запуск по умолчанию: ./start.py --protocol https --host 192.168.1.1 --port 8443 --login admin --passwd radmin

import sys
import re
import json
import requests
from terminaltables import AsciiTable
import progressbar
import time
from datetime import datetime

# Библиотека запросов
import librequests
# Библиотека парсеров
import parser_sysifaces_interfaces
import parser_netstatus_interfaces

print ('\x1b[1;32;40m' + datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + ' скрипт запущен: ' + '\x1b[0m')

# Читаем переменные переданные в скрипт
arg_all_ = ''
for arg_ in sys.argv:
	arg_all_ += str(arg_) + ' '
#print (arg_all_)

# С помощью регулярных вырожений назначаем значение параметров
try:
	protocol_ = str(re.findall(r'--protocol.(\w+)', arg_all_, re.MULTILINE|re.DOTALL)[0])
	host_ = str(re.findall(r'--host.(\d+.\d+.\d+.\d+)', arg_all_, re.MULTILINE|re.DOTALL)[0])
	port_ = str(re.findall(r'--port.(\d+)', arg_all_, re.MULTILINE|re.DOTALL)[0])
	login_ = str(re.findall(r'--login.(\w+)', arg_all_, re.MULTILINE|re.DOTALL)[0])
	password_ = str(re.findall(r'--passwd.(\w+)', arg_all_, re.MULTILINE|re.DOTALL)[0])
except:
	print ('Ошибка, заданы не все параметры: ' + arg_all_)
	print ('Формат: ./start.py --protocol https --host 192.168.1.1 --port 8443 --login admin --passwd radmin')
	exit()

print ('----------------------------------------------------------')
print ('IP-address = ' + protocol_ + '://' + host_ + ':' + port_)
print ('login = ' + login_)
print ('password = ' + password_)

# Чтение параметров из файла
print ('----------------------------------------------------------')
print ('\x1b[1;32;40m' + ' Шаг-1: Загрузка параметров ' + '\x1b[0m')

parameters_file_ = 'parameters.json'
try:
	with open(parameters_file_, 'r', encoding='utf-8') as read_file_:
		parameters_ = json.load(read_file_)
	print (parameters_['name'])
	print ('Описание: ' + parameters_['description'])
	timeout_ = parameters_['timeout']
	timeout_start_ = parameters_['timeout_start']
	print ('Время ожидания ответа от Рубикон: ' + str(timeout_) + ' сек')
	print ('Время ожидания загрузки Рубикон: ' + str(timeout_start_) + ' сек')
	#print (parameters)
except:
	print ('Ошибка чтения файла конфигурации: ' + parameters_file_)
	exit()

# Чтение словаря из файла
print ('----------------------------------------------------------')
print ('\x1b[1;32;40m' + ' Шаг-2: Загрузка словаря ' + '\x1b[0m')

dictionary_file_ = 'dictionary.json'
try:
	with open(dictionary_file_, 'r', encoding='utf-8') as read_file_:
		dictionary_ = json.load(read_file_)
	#print (dictionary)
	print ('Количество проверок в словаре: ' + str(len(dictionary_)))
except:
	print ('Ошибка чтения словаря: ' + dictionary_file_)
	exit()

# Тест-кейс проверки
# проверяем post-запросы
print ('----------------------------------------------------------')
print ('\x1b[1;32;40m' + ' Шаг-3: Проверка post-запросов с параметрами по умолчанию: ' + '\x1b[0m')

description_ = str(parameters_['post']['sysifaces_interfaces']['description'])
urn_ = str(parameters_['post']['sysifaces_interfaces']['urn'])
data_ = parameters_['post']['sysifaces_interfaces']['data'].copy()

print ('Описание: ' + description_)
print ('URL: ' + protocol_ + '://' + host_ + ':' + port_ + urn_)
print ('Параметры: ' + str(data_))

req_ = librequests.post(protocol_, host_, port_, urn_, login_, password_, timeout_, data_)
print ('Код ответа сервера: ' + str(req_))

print ('----------------------------------------------------------')
print ('\x1b[1;32;40m' + ' Шаг-4: Проверка get-запросов и парсеров с параметрами по умолчанию: ' + '\x1b[0m')

# Парсер для sysifaces
description_ = str(parameters_['get']['sysifaces']['description'])
urn_ = str(parameters_['get']['sysifaces']['urn'])
print ('Описание: ' + description_)

req_ = librequests.get(protocol_, host_, port_, urn_, login_, password_, timeout_)

if type(req_) == requests.models.Response:
    print ('Код ответа сервера: ' + str(req_.status_code))
    net_ = parser_sysifaces_interfaces.parsing(req_.text)
else:
    net_ = 'error'

print ('Результат парсинга страницы ' + protocol_ + '://' + host_ + ':' + port_ + urn_ + ' :')
table_data_ = [['Имя', 'Цвет', 'Номер', 'IP-адресс', 'Маска сети', 'MAC-адрес','MTU']]
for i_ in net_:
    table_data_.append([i_['name'], i_['color'], i_['number'], i_['address'], i_['netmask'], i_['mac'], i_['mtu']])
print (AsciiTable(table_data_).table)
print ('')

# Парсер для netstatus
description_ = str(parameters_['get']['netstatus']['description'])
urn_ = str(parameters_['get']['netstatus']['urn'])
print ('Описание: ' + description_)

req_ = librequests.get(protocol_, host_, port_, urn_, login_, password_, timeout_)

if type(req_) == requests.models.Response:
    print ('Код ответа сервера: ' + str(req_.status_code))
    net_ = parser_netstatus_interfaces.parsing(req_.text)
else:
    net_ = 'error'

print ('Результат парсинга страницы ' + protocol_ + '://' + host_ + ':' + port_ + urn_ + ' :')
table_data_ = [['Имя', 'Статус', 'IP-адресс', 'Маска сети', 'MAC-адрес','MTU']]
for i_ in net_:
    table_data_.append([i_['name'], i_['status'], i_['address'], i_['netmask'], i_['mac'], i_['mtu']])
print (AsciiTable(table_data_).table)

print ('----------------------------------------------------------')
print ('\x1b[1;32;40m' + ' Шаг-5: Определяем имя интерфейса: ' + '\x1b[0m')
urn_ = str(parameters_['get']['sysifaces']['urn'])
data_ = parameters_['post']['sysifaces_interfaces']['data'].copy()
req_ = librequests.get(protocol_, host_, port_, urn_, login_, password_, timeout_)
if type(req_) == requests.models.Response:
    print ('Код ответа сервера: ' + str(req_.status_code))
    net_ = parser_sysifaces_interfaces.parsing(req_.text)
else:
    net_ = 'error'
interface_name_ = ''
for i_ in net_:
    if str(i_['color']) == str(data_['COLOR']) and str(i_['number']) == str(data_['NUMBER']) and str(i_['address']) == str(data_['ADDRESS']):
       interface_name_ = i_['name']
print ('Имя интерфейса для которого производится проверка: ' + interface_name_)

print ('----------------------------------------------------------')
print ('\x1b[1;32;40m' + ' Шаг-6: Проверка по словарю: ' + '\x1b[0m')

# post-запрос на изменение параметров

bar_ = progressbar.ProgressBar(maxval=(len(dictionary_)+1), widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar_.start()
number_ = 0

table_data_ = [['Имя', 'Описание', 'Тип', 'Параметр', 'Ожидаемый', 'Код post', 'Фактический (sysifaces)', 'Фактический (netstatus)', 'Результат']]

for i_ in dictionary_:
    # Перед проверкой выставляем значение по умолчанию:
    urn_ = str(parameters_['post']['sysifaces_interfaces']['urn'])
    data_ = parameters_['post']['sysifaces_interfaces']['data'].copy()
    req_ = librequests.post(protocol_, host_, port_, urn_, login_, password_, timeout_, data_)
    #req_ = librequests.post(protocol_, host_, port_, urn_, login_, password_, timeout_, data_def_)

    # Назначение переменной из словаря
    #data_ = data_def_.copy()
    data_['ADDRESS'] = i_['parameter']
    code_post_ = librequests.post(protocol_, host_, port_, urn_, login_, password_, timeout_, data_)
    
    # Парсер для sysifaces 
    urn_ = str(parameters_['get']['sysifaces']['urn'])
    req_ = librequests.get(protocol_, host_, port_, urn_, login_, password_, timeout_)
    if type(req_) == requests.models.Response:
        net_ = parser_sysifaces_interfaces.parsing(req_.text)
    else:
        net_ = 'error'
    for k_ in net_:
        #print (interface_name_ + ' - ' + str(k_))
        if interface_name_ == str(k_['name']):
            address_sysifaces_ =  str(k_['address'])
            break
        else:
            address_sysifaces_ = 'none'
    
    # Парсер для netstatus
    urn_ = str(parameters_['get']['netstatus']['urn'])
    req_ = librequests.get(protocol_, host_, port_, urn_, login_, password_, timeout_)
    if type(req_) == requests.models.Response:
        net_ = parser_netstatus_interfaces.parsing(req_.text)
    else:
        net_ = 'error'
    for k_ in net_:
        #print (interface_name_ + ' - ' + str(k_['name']))
        if interface_name_ == str(k_['name']):
            address_netstatus_ =  str(k_['address'])
            break
        else:
            address_netstatus_ = 'none'
    
    # Сравнение результатов:
    if address_sysifaces_ == str(i_['valid']) and address_netstatus_ == str(i_['valid']):
        diff_status_ = '\x1b[1;32;40m' + ' ok ' + '\x1b[0m'
    else:
        diff_status_ = '\x1b[1;31;40m' + ' error ' + '\x1b[0m'
    
    table_data_.append([i_['name'], i_['description'], i_['type'], data_['ADDRESS'], i_['valid'], code_post_, address_sysifaces_, address_netstatus_, diff_status_])
    # Прогресс бар
    bar_.update(number_ + 1)
    number_ += 1
bar_.finish()

print ('----------------------------------------------------------')
print ('\x1b[1;32;40m' + ' Шаг-7: Вывод результата: ' + '\x1b[0m')
print (AsciiTable(table_data_).table)

print ('\x1b[1;32;40m' + datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + ' скрипт завершен' + '\x1b[0m')