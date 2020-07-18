#hbo fan how to install: pip3 install simple-pid

from simple_pid import PID
import os
import time
import RPi.GPIO as GPIO
import configparser

def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	temp =(res.replace("temp=","").replace("'C\n",""))
	#print("temp is {0}".format(temp)) #Uncomment here for testing
	return temp


PWM_FREQ = 80	#change this if fan stutters or else behave strange
fanPin = 21 # The pin ID, edit here to change it
GPIO.setmode(GPIO.BCM)
GPIO.setup(fanPin, GPIO.OUT)
GPIO.setwarnings(False)
myPWM=GPIO.PWM(fanPin,PWM_FREQ)
myPWM.start(50)
pid = PID(-2, -0.8, -2)
pid.setpoint = 45
output=0
pid.auto_mode = True

# assume we have a system we want to control in controlled_system

pid.sample_time = 0.5  # update every 0.01 seconds
pid.output_limits = (0, 100)    # output value will be between 0 and 10


while True:
	input_temp = float(getCPUtemperature())
	print (input_temp) 
	# compute new output from the PID according to the systems current value
	output = int(pid(input_temp)) 
	
    # feed the PID output to the system and get its current value
	#v = getCPUtemperature().update(0)
	myPWM.ChangeDutyCycle(output)
	print (output)
	time.sleep(1)

#except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt 
	#GPIO.cleanup() # resets all GPIO ports used by this program
	#myPWM.ChangeDutyCycle(0)