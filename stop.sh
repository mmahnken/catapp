#!/bin/bash

set -o errexit        # stop script on any error

pkill -F server.pid

echo -e "\nStopped.\n"
