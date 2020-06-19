#!/usr/bin/env python

import time
import Adafruit_SSD1306
import RPi.GPIO as GPIO
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import subprocess, os

def display_time():
	# Collect current time and date
	if(time_format):
		current_time = time.strftime("%H:%M:%S")
	else:
		current_time = time.strftime("%H:%M")
		
	current_date = time.strftime("%d/%m/%Y")
				
	# Clear image buffer by drawing a black filled box
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	# Set font type and size
	font = ImageFont.truetype('/home/pi/scripts/Minecraftia.ttf', 16)
	#font = ImageFont.load_default()
	# Position time
	x_pos = (disp.width/2)-(string_width(font,current_time)/2)
	y_pos = 2 + (disp.height-4-8)/2 - (35/2)
        
	# Draw time
	draw.text((x_pos, y_pos), current_time, font=font, fill=255)

	# Set font type and size
	font = ImageFont.truetype('/home/pi/scripts/Minecraftia.ttf', 8)
	#font = ImageFont.load_default()
	# Position date
	x_pos = (disp.width/2)-(string_width(font,current_date)/2)
	y_pos = disp.height-10

	# Draw date
	draw.text((x_pos, y_pos), current_date, font=font, fill=255)

	# Draw the image buffer
	disp.image(image)
	disp.display()
def display_network():
	# Collect network information by parsing command line outputs
	#ipaddress = os.popen("ifconfig wlan0 | grep 'inet addr' | awk -F: '{print $2}' | awk '{print $1}'").read()
	cmd = "hostname -I | cut -d\' \' -f1"
	ipaddress = subprocess.check_output(cmd, shell = True )
	
	#netmask = os.popen("ifconfig wlan0 | grep 'Mask' | awk -F: '{print $4}'").read()
	gateway = os.popen("route -n | grep '^0.0.0.0' | awk '{print $2}'").read()
	ssid = os.popen("iwconfig wlan0 | grep 'ESSID' | awk '{print $4}' | awk -F\\\" '{print $2}'").read()

	# Clear image buffer by drawing a black filled box
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	padding = -2
	top = padding
	bottom = height-padding
	x = 0
	# Set font type and size
        #font = ImageFont.truetype('fonts/Minecraftia.ttf', 8)
        font = ImageFont.load_default()
	# Draw SSID
	draw.text((x, top), "SSID: "+ssid, font=font, fill=255)
	# Draw IP
	draw.text((x, top+8), "IP: "+ipaddress, font=font, fill=255)
	# Draw NM
	#draw.text((x, top+16), "NM: "+netmask, font=font, fill=255)
	# Draw GW
	draw.text((x, top+16), "GW: "+gateway, font=font, fill=255)
	
	# Draw the image buffer
	disp.image(image)
	disp.display()
	
def display_stats():
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	#font = ImageFont.truetype('fonts/Minecraftia.ttf', 8)
	font = ImageFont.load_default()
	cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
	CPU = subprocess.check_output(cmd, shell = True )
	cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
	MemUsage = subprocess.check_output(cmd, shell = True )
	cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
	Disk = subprocess.check_output(cmd, shell = True )
	cmd = "vcgencmd measure_temp |cut -f 2 -d '='"
	temp = subprocess.check_output(cmd, shell = True )
		# Write two lines of text.

	draw.text((0, -2),     "CPU temp: "+ str(temp),  font=font, fill=255)
	draw.text((0, 6),     str(CPU) , font=font, fill=255)
	draw.text((0, 14),    str(MemUsage),  font=font, fill=255)
	draw.text((0, 22),    str(Disk),  font=font, fill=255)

	# Display image.
	disp.image(image)
	disp.display()
	time.sleep(.5)



def display_black():
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	#font = ImageFont.truetype('fonts/Minecraftia.ttf', 8)
	font = ImageFont.load_default()
	x = 0
	y = 0
	draw.text((x, y), "turn off screen", font=font, fill=255)
	draw.text((x, 8), "Press action key", font=font, fill=255)
	
	disp.image(image)
	disp.display()
def display_shutdown():
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	#font = ImageFont.truetype('fonts/Minecraftia.ttf', 8)
	font = ImageFont.load_default()
	x = 0
	y = 0
	draw.text((x, y), ">>>turn off PI<<<", font=font, fill=255)
	draw.text((x, 8), "Press action key", font=font, fill=255)
	
	disp.image(image)
	disp.display()
	



def display_custom(text):
	# Clear image buffer by drawing a black filled box
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	# Set font type and size
        #font = ImageFont.truetype('fonts/Minecraftia.ttf', 8)
        font = ImageFont.load_default()
        # Position SSID
        x_pos = (width/2) - (string_width(font,text)/2)
	y_pos = (height/2) - (8/2)

	# Draw SSID
	draw.text((x_pos, y_pos), text, font=font, fill=255)

	# Draw the image buffer
	disp.image(image)
	disp.display()
	
def string_width(fontType,string):
	string_width = 0

	for i, c in enumerate(string):
		char_width, char_height = draw.textsize(c, font=fontType)
		string_width += char_width

	return string_width

# Set up GPIO with internal pull-up
GPIO.setmode(GPIO.BCM)	
#GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

select_switch = 12  # pin 18 connect to ground
action_switch = 16 #shutdown switch, connect to ground
#GPIO.setup(select_switch,GPIO.IN)
GPIO.setup(select_switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(action_switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

	
# 128x64 display with hardware I2C
#disp = Adafruit_SSD1306.SSD1306_128_64(rst=24)
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Initialize library
disp.begin()

# Get display width and height
width = disp.width
height = disp.height

# Clear display
disp.clear()
disp.display()

# Create image buffer with mode '1' for 1-bit color
image = Image.new('1', (width, height))

# Load default font
font = ImageFont.load_default()

# Create drawing object
draw = ImageDraw.Draw(image)

prev_millis = 0
prev_social = 0
display = 0
time_format = True
#black_out = True

while True:
	millis = int(round(time.time() * 1000))

	# Software debouncing
	if((millis - prev_millis) > 250):
		# Cycle through different displays
		if(not GPIO.input(select_switch)):
			disp.command(Adafruit_SSD1306.SSD1306_DISPLAYON)
			display += 1
			if(display > 4):
				display = 0
			prev_millis = int(round(time.time() * 1000))

		# Trigger action based on current display
		elif(not GPIO.input(action_switch)):
			if(display == 0):
				# Toggle between 12/24h format
				time_format =  not time_format
				time.sleep(0.01)
			elif(display == 1):
				# Reconnect to network
				display_custom("reconnecting wifi ...")
				os.popen("sudo ifdown wlan0; sleep 5; sudo ifup --force wlan0")
				time.sleep(0.01)
			elif(display == 2):#no action key yet
				time.sleep(0.01)
			elif(display == 3):
				disp.command(Adafruit_SSD1306.SSD1306_DISPLAYOFF)
				time.sleep(0.01)
			elif(display == 4):
				display_custom("Shutdown in 5 secs")
				time.sleep(1)
				display_custom("Shutdown in 3 secs")
				time.sleep(1)
				display_custom("Shutdown in 2 secs")
				time.sleep(1)
				display_custom("Shutdown in 1 secs")
				time.sleep(1)
				display_custom("Shutdown in 0 secs")
				time.sleep(0.5)
				disp.command(Adafruit_SSD1306.SSD1306_DISPLAYOFF)
				os.system("sudo shutdown -h now")
			prev_millis = int(round(time.time() * 1000))

	if(display == 0):
		display_time()
		prev_shutdown = 0
	elif(display == 1):
		display_network()
		prev_shutdown = 0
	elif(display == 2):
		display_stats()
		prev_shutdown =0
	elif(display == 3):
		display_black()
		prev_shutdown = 0
	elif(display == 4):
		display_shutdown()
		
	time.sleep(0.1)