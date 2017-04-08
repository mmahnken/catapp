#!/bin/bash

set -o errexit 

pkill -F server.pid

echo -e "\nStopped.\n"
