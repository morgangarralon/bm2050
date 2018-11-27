#!/bin/bash


#nohup uwsgi --ini /home/ubuntu/bm2050/uwsgi.ini &
/home/ubuntu/bm2050/stop_server.sh
sleep 3

echo "starting uwsgi app"
cd /tmp
#exec uwsgi --ini /home/ubuntu/bm2050/uwsgi.ini
nohup uwsgi --ini /home/ubuntu/bm2050/uwsgi.ini &
