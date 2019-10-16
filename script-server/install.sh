#!/bin/bash

HOME_DIR="/home/"
NAME="script-server"

echo "create directory $HOME_DIR$NAME"
mkdir $HOME_DIR$NAME

echo "download script-server from github"
wget https://github.com/bugy/script-server/releases/download/1.14.0/script-server.zip

echo "unzip script-server"
unzip script-server.zip -d $HOME_DIR$NAME

echo "install python3"
apt-get install python3

echo "install pip3"
apt-get install python3-pip

SCRIPT_DIR=$(dirname $0)
echo "dir script = $SCRIPT_DIR"

echo "cp files"
cp $SCRIPT_DIR/start.sh $HOME_DIR$NAME -v
cp $SCRIPT_DIR/script-server.json $HOME_DIR$NAME -v
cp $SCRIPT_DIR/script-server /etc/init.d/ -v
cp $SCRIPT_DIR/script-server.service /etc/systemd/system/ -v

echo "enable script-server"
systemctl enable script-server.service