#!/bin/bash
#this is only if every minute isn't fast enough for you :)
#This runs every 5 seconds. Just change the path and run it in the background
# ./website.sh & <== To run in background
while True
do
    python /path/to/file
    sleep 5
done
