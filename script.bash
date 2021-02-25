#!/bin/bash 
echo "Starting ecs-verification..."
while true
do
    sleep 60
    result=`python main.py check_containers`
    if [ "$result" == "All containers terminated! ;)" ]; then
        echo "All containers terminated! ;)"
        exit 1
    else 
        echo $result
    fi
done
