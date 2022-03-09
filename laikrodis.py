import RPi.GPIO as GPIO
import time
from datetime import datetime
from astral import Astral


#          0,  1, 2,  3,  4,  5,  6,  7,  8,  9, 10, 11
outputs = [2,  3, 4, 14, 15, 17, 18, 27, 22, 23, 24, 10]
borderLamps = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(outputs, GPIO.OUT)
GPIO.setup(borderLamps, GPIO.OUT)


def show_time_v1():
	while True:
		hour = datetime.now().hour


		a = Astral()
		a.solar_depression = 'civil'
		sun = a['Vilnius'].sun(date=datetime.now(), local=True)
		sunrise = sun['sunrise'].time().hour + 1
		sunset = sun['sunset'].time().hour - 1


		if(hour<=sunrise or hour>=sunset):
			GPIO.output(borderLamps, GPIO.HIGH)


			if hour > 12:
				hour = hour - 12 - 1
			elif hour > 0:
				hour = hour - 1
			else:
				hour = 11

			for output in outputs:
				GPIO.output(output, GPIO.LOW)

			GPIO.output(outputs[hour], GPIO.HIGH)
			print("Lamp (0..11): " + str(hour) )


		else:
			GPIO.output(borderLamps, GPIO.LOW)
			for output in outputs:
				GPIO.output(output, GPIO.LOW)
			print("Turned OFF. Sunrise: " + str(sunrise) + " Sunset: " + str(sunset))


		time.sleep(3)



def test():
	while True:
		for output in outputs:
			GPIO.output(output, GPIO.HIGH)
			time.sleep(0.1)
		for output in outputs:
			GPIO.output(output, GPIO.LOW)
			time.sleep(0.1)

show_time_v1()
#test()
