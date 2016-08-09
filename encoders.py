#Benjamin Ramirez
#August 3, 2016

import dc_motors
import RPi.GPIO as GPIO

#testing out the encoders from polulu 25mmD gearmotos
#creating threads with interrupt routines for BOTH rising and falling edges
#this should create the maximum number of ticks per wheel
# the motor: https://www.pololu.com/product/2273
FORWARD = 1
BACKWARD = 2
GPIO.setmode(GPIO.BCM)
M1_PINS = [22,23]
M2_PINS = [16,19]

for x in range(len(M1_PINS)):
    GPIO.setup(M1_PINS[x], GPIO.IN)
    GPIO.setup(M2_PINS[x], GPIO.IN)

global CNT_1, CNT_2
CNT_1 = 0
CNT_2 = 0
#since it has 2 pins per motor, we will call the same functions for both A and B
#this will reduce the interrupts to 2 different functions
# one for A2 + B2 on motor1, another for A2 + B2 on motor2

def m1_call(channel):
    global CNT_1
    print "edge detected on M1"
    CNT_1 += 1

def m2_call(channel):
    global CNT_2
    print "edge detected on M2"
    CNT_2 += 1

#setting up the events for the pins
for x in range(len(M1_PINS)):
    GPIO.add_event_detect(M1_PINS[x], GPIO.BOTH, callback=m1_call)
    GPIO.add_event_detect(M2_PINS[x], GPIO.BOTH, callback=m2_call)

#creating the motors object, moving them forward

motors = dc_motors.DC_MOTORS()

print "Making the robot Move, checking how many edges detected"

try:
    motors.move(FORWARD,FORWARD,150,0,4)
    motors.stop()
    print CNT_1, CNT_2

finally:
    GPIO.cleanup()
               
