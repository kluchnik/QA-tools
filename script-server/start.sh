#!/bin/bash

/usr/bin/python3 /home/script-server/launcher.py -f /home/script-server/script-server.json > /dev/null & echo $! > /var/run/script-server.pid
