#!/bin/bash
cd /home/$USER/AwesomeAutoNews/
STR=0
#Set the FREQ variable to determine how often you want to get the updates
FREQ=2
while (( $STR < $FREQ ))
do
$((++STR))
python3 AutoNews.py
sleep 1h
done
