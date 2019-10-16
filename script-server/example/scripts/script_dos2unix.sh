#!/bin/bash

file=$1

echo 'имя файла:' $file

date=$(date +%Y.%m.%d' '%H:%M:%S)
echo -e "\x1b[0;32;40m $date скрипт запущен:\x1b[0m"

dos2unix $file
chmod 777 $file
chmod +x $file

echo -e "\x1b[0;32;40m $date скрипт завершен\x1b[0m"
