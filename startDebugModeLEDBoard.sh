#!/bin/bash
#
# Start the webserver.
#
WsBase=./www-logs/webserver-0.0.0.0-8080
PidFile=$WsBase.pid
if [ -f $PidFile ] ; then
    Pid=$(cat $PidFile)
    if kill -0 $Pid 2>&1 >/dev/null ; then
	echo "ERROR: webserver is already running, PID=$Pid"
	exit 1
    else
	# The process does not exist, remove the pid file.
	rm -f $PidFile
    fi
fi
./start.py -H 0.0.0.0 -p 8080 -l debug --no-dirlist -r ./ -d ./www-logs

echo "started"
