#!/bin/bash
#this is only if every minute isn't fast enough for you :)
#This runs every 5 seconds. Just change the path and run it in the background
# ./website.sh & <== To run in background
while true
do
    python /home/ec2-user/website_status/web_status.py
    sleep 5
done
