#!/usr/bin/python
#Benjamin Ramirez 08/02/2016
#Creating a class to handle the pwm signals for 2 DC motors
#utilizing some functions from adafruit site for the motor hat:
#https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/using-dc-motors
#used portions from Tony DiCola's Robot.py file inside /examples/

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

#creating a class to control 2 dc motors using the Adafruit_MotorHat
class DC_MOTORS(object):
	def __init__(self, addr=0x60, left_id=2, right_id=1, stop_at_exit=True):
		"""creating an object to control 2 dc motors, 
		-addr: The I2C address of the motor HAT
		- left_id: the ID of the left motor, (1)
		- right_id: the ID of the right motor, (2)
		-stop_at_exit: flag used to indicate that motors should stop when the program exits(
		(want to prevent a crash ofc)
		"""
		#initializing the motors
		self._mh = Adafruit_MotorHAT(addr)
		self._left = self._mh.getMotor(left_id)
		self._right = self._mh.getMotor(right_id)
		#init motors to off
		self._left.run(Adafruit_MotorHAT.RELEASE)
		self._right.run(Adafruit_MotorHAT.RELEASE)
		#setting the atexit function for when the program exits
		if stop_at_exit:
			atexit.register(self.stop)

# recommended for auto-disabling motors on shutdown!

	def _left_speed(self, speed):
		#change the voltage to motor
		assert 0 <= speed <=255
		speed = max(0, min(255, speed))
		self._left.setSpeed(speed)

	def _right_speed(self, speed):
		#change the voltage to motor
		assert 0 <= speed <=255
		speed = max(0, min(255, speed))
		self._right.setSpeed(speed)

	def stop(self):
		self._left.run(Adafruit_MotorHAT.RELEASE)
		self._right.run(Adafruit_MotorHAT.RELEASE)
	

	def move(self, dir_1, dir_2, speed_1, speed_2, seconds=None):
		self._left_speed(speed_1)
		self._right_speed(speed_2)
		self._left.run(dir_1)
		self._right.run(dir_2)
		#only moving for a specified time if the seconds parameter is passed
		if seconds is not None:
			time.sleep(seconds)
			self.stop()
	
	def _left_dir(self, dir):
		self._left.run(Adafruit_MotorHAT.dir)
	
	def _right_dir(self, dir):
		self._right.run(Adafruit_MotorHAT.dir)
		
	
