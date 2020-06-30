# AwesomeAutoNews

## An application to recieve automatic updates about anything!
This application is a program which can let you recieve updates about pretty much anything and you can set it to be fully automatic or partially automatic.

## Prerequisites

Most of the commands and scripts are for linux and this will work only on linux.

1. You will need tkinter, pyautogui, subprocess, PIL and webbrowser python libraries and probably other ones which I might have missed out.

2. I can upload a compiled executable single file of the format .sh if needed. So if you need that just let me know, or if you know how to do it you
can do that yourself.

## Features

1. There is a manual version and an automatic version

2. In the manual version you type in the thing of which you want to get the update and it will open the subject in the browser (firefox by default and can be changed in 
the source code, will make a more compatible version in the future), takes a screen shot and displays it to you inside the gui application itself.

3. The screenshot images are automatically removed upon closing but a manual button is also present just in case. The images are automatically removed to prevent any conflict.

4. The automatic version asks you for input the first time after which, everytime it is opened, it will automatic search without having to ask for input. There is a reset and 
set button to change the initial search query that had been set. To do this, first press reset and type in the query and press set.

5. A timer bash script is present which automatically opens the python application every x min/hour/etc and for a set number of times. This script can be added to the startup
script which will make it fully automatic.

6. Whenever the python application works, the date and time are logged into the time_entries.txt file and this is to make sure that the time frequency of the script is working
properly.

7. You can set the EXEC path in the desktop entry to any of the .py or .sh files. More desktop entries and icons will be coming in the future.

## Instructions

1. Clone this repo by using the command, `git clone https://github.com/frankstan33127/AwesomeAutoNews.git` while in your home/user/ directory in the terminal.

2. Change the path of ICON in the desktop entry to make it working. And you're good to go!

3. You can add this script in the startup to make it run after every boot.

4. Make all the .sh and .py executable by going into the properties.

## Notes

1. Feel free to modify, redistribute, reproduce, etc this project. 

1. All the icons were created by myself.

