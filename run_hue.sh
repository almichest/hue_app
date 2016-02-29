#!/bin/sh
python3 src/application.py
if [ $? != 0 ] ; then
    echo 'App crashed with error'.
    python3 src/error_twitter.py
fi
