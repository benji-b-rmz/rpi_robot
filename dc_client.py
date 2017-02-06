#Author: Benjamin Ramirez
#August 3, 2016
# creating a client to test out dc_motor class functions
import sys, os
import time
from actuators import dcmotors
from sensors import encoders, rangers
import RPi.GPIO as GPIO

FORWARD = 1
BACKWARD = 2

motors = dcmotors.Motors()
encoder1 = encoders.Encoder(22,23)
encoder2 = encoders.Encoder(16,19)
#created the new motors object
try:
    print "\nMoving the motors for 5 sec, FORWARD Dir\n"
    motors.move(BACKWARD,FORWARD,150,150,3)
    print "ticks:", encoder1.get_ticks(), encoder2.get_ticks()
    motors.stop()

    encoder1.reset()
    encoder2.reset()

    motors.move(BACKWARD, BACKWARD, 200,200, 1)
    print encoder1.get_ticks(), encoder2.get_ticks()
#print "now, moving the right motor backwards"
#motors.move(FORWARD,BACKWARD,150,150,3)
finally:
    pass


