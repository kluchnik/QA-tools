#!/usr/bin/python3

import requests
from datetime import datetime
import sys
import json
import time

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host = sys.argv[1] + '://' + sys.argv[2] + ':' + sys.argv[3]
file = sys.argv[4]
print ('IP-адрес Рубикон: ' + host)
print ('Список страниц: ' + file)

def info_web(url):
    rez = ''
    try:
        start = time.time()
        r = requests.get(url, verify=False, auth=('admin','radmin'), timeout=10)
        stop = time.time()
    except:
        rez = '\t' + '\x1b[1;31;40m host unreachable \x1b[0m'
    else:
        rez = '\t' + 'time = ' + str(stop - start)[0:10] + '\t' + 'ftime = ' + str(r.elapsed) + '\t code = ' + str(r.status_code)
        if r.status_code == 200:
            rez = rez + '\t' + '\x1b[1;32;40m' + ' OK ' + '\x1b[0m'
        else:
            rez = rez + '\t' + '\x1b[1;31;40m' + ' ERROR ' + '\x1b[0m'
    return rez

print ('\x1b[1;32;40m' + datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + ' скрипт запущен: ' + '\x1b[0m')

with open(file, 'r') as f:
    data = json.loads(f.read())
    for i in data['parameters']:
        print (i['name'].ljust(50) + i['url'].ljust(40), end = ' ')
        print (info_web(host + i['url']))

print ('\x1b[1;32;40m' + datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + ' скрипт завершен' + '\x1b[0m')