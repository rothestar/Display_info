# Display_info
Get Raspberry pi info and send them to a 0.96" Oled display


How to install and setup:
at promps

git clone https://github.com/rothestar/hboscripts.git


change rc.local

command:
sudo nano /etc/rc.local

add following lines:

sudo python /home/pi/hboscripts/infodisplay/infodisplay4.py &

sudo python /home/pi/hboscripts/fan/fan_ctrl.py &
exit 0

ctrl+x to save changes

to reboot:
sudo reboot


to update:
cd /home/pi/hboscripts/
git init
git pull https://github.com/rothestar/hboscripts.git

