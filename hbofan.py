#!/usr/bin/env python3
#hbo fan how to install: pip3 install simple-pid
# https://pypi.org/project/simple-pid/

from simple_pid import PID
import os
import time
import RPi.GPIO as GPIO
import configparser

###########################################################
#settingsfile section Begin
###########################################################


#app_name = "hboscripts"

#config_folder = os.path.join(os.path.expanduser("~"), '.config', app_name)
config_folder = os.path.dirname(os.path.abspath(__file__))

#os.makedirs(config_folder, exist_ok=True)
settings_file = "settings.conf"
full_config_file_path = os.path.join(config_folder, settings_file)
#print(full_config_file_path) 
config = configparser.ConfigParser()
 
###########################################################
##settingsfile section END
###########################################################





def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	temp =(res.replace("temp=","").replace("'C\n",""))
	#print("temp is {0}".format(temp)) #Uncomment here for testing
	return temp

	
PWM_FREQ = config['User'].getint('fan_frequency')	
fanPin = 21 # The pin ID, edit here to change it
GPIO.setmode(GPIO.BCM)
GPIO.setup(fanPin, GPIO.OUT)
GPIO.setwarnings(False)
myPWM=GPIO.PWM(fanPin,PWM_FREQ)
#myPWM.start(50)

#pid = PID(-3, -0.5, -2.5)
pid.Kp=config['User'].getint('fan_pid_kp')
pid.Ki=config['User'].getint('fan_pid_ki')
pid.Kd=config['User'].getint('fan_pid_kd')


pid.setpoint = config['User'].getint('fan_set_temp')
output=0
pid.auto_mode = True
pid.sample_time = 0.5  # update every 0.01 seconds
pid.output_limits = (0, 100)    # output value will be between 0 and 10


while True:
	pid.setpoint = 45
	input_temp = float(getCPUtemperature())
	#print (input_temp) 
	# compute new output from the PID according to the systems current value
	output = int(pid(input_temp)) 
	
    # feed the PID output to the system and get its current value
	#v = getCPUtemperature().update(0)
	myPWM.ChangeDutyCycle(output)
	#print (output)
	time.sleep(1)

