#!/usr/bin/bash
# Write a Bash script that takes in a URL,and the size of the body of the response
echo $(curl -sI "$1" | grep "Content-Length" | awk '{print $2}')
