import RPi.GPIO as GPIO
import sys

pin = int(sys.argv[1])
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

with open("/sys/class/gpio/gpio7/value") as pins:
    status = pins.read(1)

if status == 1:
	print("pin is high")
else:
	print("pin is low")
