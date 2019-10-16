#!/bin/bash

HOME_DIR="/home/"
NAME="script-server"

SCRIPT_DIR=$(dirname $0)
echo "dir script = $SCRIPT_DIR"

echo "cp example"
cp -r $SCRIPT_DIR/example/* $HOME_DIR$NAME/conf/ -v

echo "chmod example"
chmod -R 777 $HOME_DIR$NAME/conf/
