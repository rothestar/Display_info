# Display_info
got my insparation fron this website http://frederickvandenbosch.be/?p=1365

And this instructable: https://www.instructables.com/id/PWM-Regulated-Fan-Based-on-CPU-Temperature-for-Ras/

Did some changes to codes to fit my demands.. the goal is to make the best headless setup... more to come

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

