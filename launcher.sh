#!/bin/sh
#launcher.sh # navigate to home directory, then to this directory, then execute python script, then back home
locale
cd 
cd /home/pi/hboscripts/
sudo python3 ./infodisplay4.py &
sudo python3 ./hbofan.py &
cd
 