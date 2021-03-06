#Benjamin Ramirez
#August 9, 2016
#using the encoders for odometry, pose(x, y, theta)

import sys, os, time
from actuators import dcmotors
from sensors import encoders
import RPi.GPIO as GPIO
import math

FORWARD = 1
BACK = 2
left = 0.0
right = 1000.0
bottom = 0.0
top = 1000.0

#important robot dimensions
TPR = 1632.67 #ticks per rotation may need to multiply by 2 https://www.pololu.com/product/2273
RW = 36.5 #radius of wheels (mm)
L = 165.0 #Length between centers of the two wheels (mm))
PI2 = 2*math.pi


def main():

#important odometry variables for initial pose
    dtheta = 0.0
    theta = math.pi/2
    x = 50.0
    y = 50.0
    dx = 0.0
    dy = 0.0
    motors = dcmotors.Motors()
    left_encoder = encoders.Encoder(22,23)
    right_encoder = encoders.Encoder(16,19)
    #created motors and encoder objects
    try:
        print "Moving the car"
        print "edge counts:", left_encoder.get_ticks(), right_encoder.get_ticks()
        left_encoder.reset()
        right_encoder.reset()
        motors.move(FORWARD, FORWARD, 200,200)
        while (y < 500):
            dtheta = math.pi * (RW/L) * (float(abs(left_encoder.get_ticks())-abs(right_encoder.get_ticks()))/TPR)
            theta = math.fmod(theta + dtheta, PI2)
            print theta
        
            dx = math.cos(theta) * (PI2*RW * (left_encoder.get_ticks()/TPR))
            x = x + dx
            dy = math.sin(theta) * (PI2*RW * (right_encoder.get_ticks()/TPR))
            y = y + dy
            print "cos(theta), sin(theta)", math.cos(theta), math.sin(theta)
            print "dx, dy:",  dx, dy
            print "ticks:", left_encoder.get_ticks(), right_encoder.get_ticks()
            left_encoder.reset()
            right_encoder.reset()
            print "POSE:", x, y, theta
            time.sleep(0.01)

        
        motors.move(BACK, FORWARD, 100, 200,1)
        while( theta > 0.1 ):
            dtheta = math.pi * (RW/L) * (float(abs(left_encoder.get_ticks()) - abs(right_encoder.get_ticks()))/TPR)
            theta = math.fmod(theta + dtheta, PI2)
            print theta

            dx = math.cos(theta) * (PI2*RW * (left_encoder.get_ticks()/TPR))
            x = x + dx
            dy = math.sin(theta) * (PI2*RW * (right_encoder.get_ticks()/TPR))
            y = y + dy
            print "cos(theta), sin(theta)", math.cos(theta), math.sin(theta)
            print "dx, dy:",  dx, dy
            print "ticks:", left_encoder.get_ticks(), right_encoder.get_ticks()
            left_encoder.reset()
            right_encoder.reset()
            print "POSE:", x, y, theta
            time.sleep(0.01)
        motors.move(FORWARD, FORWARD, 150, 150 )
        while( y > 0):
            dtheta = math.pi * (RW/L) * (float(abs(left_encoder.get_ticks())- abs(right_encoder.get_ticks()))/TPR)
            theta = math.fmod(theta + dtheta, PI2)
            print theta

            dx = math.cos(theta) * (PI2*RW * (left_encoder.get_ticks()/TPR))
            x = x + dx
            dy = math.sin(theta) * (PI2*RW * (right_encoder.get_ticks()/TPR))
            y = y + dy
            print "cos(theta), sin(theta)", math.cos(theta), math.sin(theta)
            print "dx, dy:",  dx, dy
            print "ticks:", left_encoder.get_ticks(), right_encoder.get_ticks()
            left_encoder.reset()
            right_encoder.reset()
            print "POSE:", x, y, theta
            time.sleep(0.01)

	motors.stop()
    finally:
        pass        
    

if __name__ == "__main__":
    main()

