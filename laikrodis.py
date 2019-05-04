import RPi.GPIO as GPIO
import time
import datetime as dt

# 0, 1, 2, 3,  4, 5, 6, 7, 8, 9, 10, 11
outputs = [2, 24, 3, 4, 14, 22, 15, 17, 18, 27, 23, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(outputs, GPIO.OUT)



def show_time_v1():
	while True:
		hour = dt.datetime.now().hour
		if hour >= 12:
			hour = hour - 12

		for output in outputs:
			GPIO.output(output, GPIO.HIGH)

		GPIO.output(outputs[hour], GPIO.LOW)
		time.sleep(3)



def test():
	while True:
		for output in outputs:
			GPIO.output(output, GPIO.HIGH)
			time.sleep(0.4)
		for output in outputs:
			GPIO.output(output, GPIO.LOW)
			time.sleep(0.4)

show_time_v1()
