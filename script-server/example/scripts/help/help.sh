#!/bin/sh

arg=$( echo $@ | sed 's/--list //g' )
echo Информация из раздела: $arg
echo

file=$( echo $arg.txt | sed 's/ /_/g' )
cat ./$file
