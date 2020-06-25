#!/bin/sh
#launcher.sh # navigate to home directory, then to this directory, then execute python script, then back home
locale
cd 
cd /home/pi/hboscripts/infodisplay/
sudo python ./infodisplay4.py &
cd
cd /home/pi/hboscripts/fan/
sudo python ./fanPWM.py &
cd
 