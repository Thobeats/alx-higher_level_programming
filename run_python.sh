#!/bin/bash

if [ -z "$PYFILE" ]; then
    echo "This enviroment does not exist"
    exit 1
fi

if [ ! -f "$PYFILE" ]; then
    echo "This file does not exist"
    exit 1
fi

python "$PYFILE"
