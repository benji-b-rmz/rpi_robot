#Benjamin Ramirez
#August 9, 2016
#using the encoders for odometry, pose(x, y, theta)

import sys, os, time
from dc_motors import DC_MOTORS
from encoder import ENCODER
import RPi.GPIO as GPIO
import math

FORWARD = 1
BACK = 2
left = 0.0
right = 1000.0
bottom = 0.0
top = 1000.0

#important car dimensions
TPR = 48 #ticks per rotation
RW = 36.5 #radius of wheels (mm)
L = 165.0 #Length between centers of the two wheels (mm))
PI2 = 2*math.pi

#important odometry variables
dtheta = 0.0
theta = math.pi/2
x = 50.0
y = 50.0
dx = 0.0
dy = 0.0
theta_trn = 0.0


def main():
   #important car dimensions
    TPR = 48 #ticks per rotation
    RW = 36.5 #radius of wheels (mm)
    L = 165.0 #Length between centers of the two wheels (mm))
    PI2 = 2*math.pi

#important odometry variables
    dtheta = 0.0
    theta = math.pi/2
    x = 50.0
    y = 50.0
    dx = 0.0
    dy = 0.0
    theta_trn = 0.0
    motors = DC_MOTORS()
    encoder1 = ENCODER(22,23)
    encoder2 = ENCODER(16,19)
    #created motors and encoder objects
    try:
        print "Moving the car"
        motors.move(FORWARD, FORWARD, 150, 150, 3)
        print "edge counts:", encoder1.get_ticks(), encoder2.get_ticks()
        encoder1.reset()
        encoder2.reset()
        motors.move(FORWARD, FORWARD, 150,150)
        while (y < 500):
            dtheta = math.pi * (RW/L) * (float(abs(encoder1.get_ticks())-abs(encoder2.get_ticks()))/TPR)
            theta = math.fmod(theta + dtheta, PI2)
            theta_trn = theta_trn + dtheta
        
            dx = math.pi * RW * math.cos(theta) * (float((encoder1.get_ticks() + encoder2.get_ticks())/TPR))
            x = x + dx
            dy = math.pi * RW * math.sin(theta) * (float((encoder1.get_ticks() + encoder2.get_ticks())/TPR))
            y = y + dy
            print "ticks:", encoder1.get_ticks(), encoder2.get_ticks()
            encoder1.reset()
            encoder2.reset()
            print "POSE:", x, y, theta

    finally:
        pass        
    

if __name__ == "__main__":
    main()
