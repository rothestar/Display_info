# Display_info
got my insparation fron this website http://frederickvandenbosch.be/?p=1365

And this instructable: https://www.instructables.com/id/PWM-Regulated-Fan-Based-on-CPU-Temperature-for-Ras/

Did some changes to codes to fit my demands.. the goal is to make the best headless setup... more to come

Get Raspberry pi info and send them to a 0.96" Oled display


How to install and setup:
at promps
sudo raspi-config

set wifi contrycode
enable I2C

sudo reboot

sudo apt install git

sudo apt install python-smbus

sudo apt install i2c-tools

sudo apt install python-setuptoolsc

sudo apt install python3-rpi.gpio

sudo apt install python3-pip

sudo apt install python3-pil

sudo pip3 install getrpimodel

pip3 install simple-pid


git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git

cd Adafruit_Python_SSD1306

sudo python3 setup.py install



git clone https://github.com/rothestar/hboscripts.git

cd /home/pi/hboscripts

make launcher executable:

chmod 755 launcher.sh

make the display start on boot:

sudo crontab –e

add the folloing line:

@reboot sh /home/pi/hboscripts/launcher.sh



ctrl+x to save changes

to reboot:
sudo reboot


to update:
cd /home/pi/hboscripts/

git init

git pull https://github.com/rothestar/hboscripts.git

