#Benjamin Ramirez
#August 4, 2016
#Writing a class for the HC_SRO4 ultrasonic range finder
#Datasheet: http://www.micropik.com/PDF/HCSR04.pdf

import time
import RPi.GPIO as GPIO
import atexit

"""Creating a range detecting object for use with HC-SRO4 module """
class ranger(object):
    
    def __init__(self, trig_pin, echo_pin, stop_at_exit=True):
        
        self.trig = trig_pin
        self.echo = echo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
        GPIO.output(self.trig, False) #initialize the output to False
        if stop_at_exit:
            atexit.register(self.stop)

    def get_dist(self):
        """we send a 10 microsecond pulse through the trigger pin
           next we wait for the pulse from the echo pin
           the length of the return pulse is proportional to the distance
        """
        #send the 10 microsecond pulse to sensor:
        GPIO.output(self.trig, True)
        time.sleep(0.00001) 
        GPIO.output(self.trig, False)

        #wait for the response (echo pulse):        
        while GPIO.input(self.echo) == 0:
            pulse_start = time.time()
        
        while GPIO.input(self.echo) == 1:
            pulse_end = time.time()
        
        #log the duration of the echo pulse
        duration = pulse_end - pulse_start
        
        #use the formula on the HC-SRO4 Datasheet to get distance
        distance = duration * 17150
        distance = round(distance,1)

        if distance > 2 and distance <= 400: #the range datasheet claims the sensor to be most accurate 
            return distance
        else:
            return 400

    def stop(self):
        GPIO.cleanup()
        
        
        
