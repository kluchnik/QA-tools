#!/bin/bash

set -e

repeats=1
text="I'm called"
filename='simple.txt'
clear=false

while (( $# >= 1 ))
do
key="$1"

case $key in
    -r)
    repeats="$2"
    echo "repeats = $repeats"
    shift # past argument
    ;;
    -t)
    text="$2"
    echo "text = $text"
    shift # past argument
    ;;
    -f)
    filename="$2"
    echo "filename = $filename"
    shift # past argument
    ;;
    --clear)
    clear=true
    ;;
    *)
    # unknown option
    ;;
esac
shift # past argument or value
done

if $clear; then
    echo "Clearing the file..."
     > /home/script-server/conf/log/"$filename"
fi

read -p "Press enter to start writing to the file (/home/script-server/conf/log/$filename)"

for (( i=0; i<repeats ; i++ ))
do
   echo "$text" >> /home/script-server/conf/log/"$filename"
done

echo "File content >> \n"
cat /home/script-server/conf/log/"$filename" | grep --color=always -E "$text|$"
