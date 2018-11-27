#!/bin/bash


echo "stoping other instances"
uwsgi --stop /tmp/uwsgi.pid
