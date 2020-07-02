#!/bin/sh
#launcher.sh # navigate to home directory, then to this directory, then execute python script, then back home
locale
cd 
cd /home/pi/hboscripts/infodisplay/
sudo python3 ./infodisplay4.py &
cd
cd /home/pi/hboscripts/fan/
sudo python3 ./fanPWM.py &
cd
 