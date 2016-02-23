#this script is called from php script using syntax:
#sudo python3 coffee.py  [pinNumber] [(1/0) on/off]
import sys, RPi.GPIO as GPIO
import time

#gets pin and bool
pin = int(sys.argv[1])
bool = int(sys.argv[2])

#sets up the out pin and GPIO board
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

if bool == 1: #Turns pin on
	GPIO.output(pin, False)
	time.sleep(3600)
	GPIO.output(pin, True)
elif bool == 0: #Turns pin off
	GPIO.output(pin, True)
