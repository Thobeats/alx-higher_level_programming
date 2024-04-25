#!/usr/bin/bash
# Write a Bash script that takes in a URL,
# sends a request to that URL, and displays
# the size of the body of the response
if [ $# == 1 ];
then
    URL=$1
    SIZE_RESPONSE=$(curl -sI "$URL" | grep "Content-Length" | awk '{print $2}')
    echo "$SIZE_RESPONSE"
fi
