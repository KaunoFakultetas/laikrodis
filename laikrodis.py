import RPi.GPIO as GPIO
import time
import datetime as dt
from threading import Timer
import math



# ------ Constants
pwmFrequency = 50 # Hz

pwmFlashFrequency = 0.3 # Hz
pwmFlashNumberOfSteps = 50 # Number of steps to perform one flash



# ------ Pins On Raspberry Board
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
hourPins = [2, 24, 3, 4, 14, 22, 15, 17, 18, 27, 23, 10] # - pin on the RPI (ex: pinOnBoard = hourPins[hour])



# ------ Initialisation of pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(hourPins, GPIO.OUT)



# ------ Low level PWM output objects
outputPwms[12]
for x in range(0, 12):
	outputPwms[x] = GPIO.PWM(hourPins[x], frequency)



# ------------------------------------------------------------------------
# ------ Built for easy output flashing control

#  1 -|         ,-'''-.
#     |      ,-'       `-.           
#     |    ,'             `.
#     |  ,'                 `.
#     | /                     \
#     |/                       \
# ----+-------------------------\--------------------------
#     |          __           __ \          __           /  __
#     |          ||/2         ||  \        3||/2        /  2||
#     |                            `.                 ,'
#     |                              `.             ,'
#     |                                `-.       ,-'
# -1 -|                                   `-,,,-'

positionInTheCycle = 0
flashingMinRange = 40
flashingMaxRange = 80
def outputFlashingCallback():

	hour = dt.datetime.now().hour
		if hour >= 12:
			hour = hour - 12


	amplitude = (flashingMaxRange - flashingMinRange) / 2
	axisX = flashingMaxRange - amplitude
	pwmAtThisMoment = axisX + amplitude * math.sin(positionInTheCycle/pwmFlashNumberOfSteps)


	outputPwms[hour].ChangeDutyCycle(pwmAtThisMoment)


	# Cycle reseter
	positionInTheCycle++
	if positionInTheCycle == pwmFlashNumberOfSteps:
		positionInTheCycle = 0

	# Infinite loop
    Timer((1/pwmFlashFrequency)/pwmFlashNumberOfSteps, timeout).start()


Timer(1/pwmFlashFrequency/pwmFlashNumberOfSteps, timeout).start()
# ------------------------------------------------------------------------


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

#show_time_v1()
