#Author: Benjamin Ramirez
#August 3, 2016
# creating a client to test out dc_motor class functions
import sys
import time
import dc_motors

FORWARD = 1
BACKWARD = 2

motors = dc_motors.DC_MOTORS()
#created the new motors object
print "\nMoving the motors for 5 sec, FORWARD Dir\n"
motors.move(FORWARD,FORWARD,150,150,3)

print "now, moving the right motor backwards"
motors.move(FORWARD,BACKWARD,150,150,3)



