#!/bin/bash
cd /home/$USER/AwesomeAutoNews/
STR=0
#Set the FREQ variable to set the amount of times you need to get the updates
FREQ=10
while (( $STR < $FREQ ))
do
$((++STR))
python3 AutoNews.py
sleep 1h
done
