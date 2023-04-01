#!/bin/sh
#

# This script is used to demonstrate the remote_sync feature of the python script
# 
# simple function to send all args to python script
wrapper() {
    python /remote_sync/main.py "$@"
}