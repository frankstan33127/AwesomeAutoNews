#!/bin/bash
cd /home/$USER/AwesomeAutoNews/
STR=0
#Set the FREQ variable to set the amount of times you need to get the updates
FREQ=10
cd 
while (( $STR < $FREQ ))
do
$((++STR))
./AutoNews.py
sleep 1h
done
