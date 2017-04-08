#!/bin/bash

set -o errexit

if [ "$#" -ne 1 ];
    then echo "error -- usage: bash start.sh port-number";
    exit 1;
fi

source env/bin/activate     # use your virtual environment

gunicorn \
    -D \
    -b 127.0.0.1:$1  \
    --log-file error.log \
    --access-logfile access.log \
    --pid server.pid \
    -n $(basename $(pwd)) \
    server:app

echo -e "\nStarted on port $1.\n"

# Those options mean:

# -D : "daemonize", run as background process

# -b : bind to this network interface and port

# --access-log-file : save visitor info in here

# --log-file : log other Flask output (errors, etc) here

# --pid : save the process ID of gunicorn here (we use this in stop.sh)

# -n : set the process title (as shown in `ps x`) to name of this app
#         (this isn't critical, but is helpful if you have several apps
#         running under gunicorn -- it makes it easy to see that this
#         instance of gunicorn is running this app)

# server:app : use a Flask/WSGI app called "app" in Python module "server"