#benjamiin ramirez August 9, 2016
#making class to keep track of encoder ticks on wheels

import RPi.GPIO as GPIO


class ENCODER(object):
    def __init__ (self, a_pin_num, b_pin_num):
        self.a_pin = a_pin_num
        self.b_pin = b_pin_num
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.a_pin, GPIO.IN)
        GPIO.setup(self.b_pin, GPIO.IN)
        self.a_ticks, self.b_ticks, self.tot_ticks = 0, 0, 0
#setting up the edge detection interrupts
        GPIO.add_event_detect(self.a_pin, GPIO.BOTH, callback=self.a_call)
        GPIO.add_event_detect(self.b_pin, GPIO.BOTH, callback=self.b_call)

    def tot_call(self):
        self.tot_ticks += 1

    def a_call(self,channel):
        #print "edge on A \n"
        self.a_ticks += 1
        self.tot_call()
    
    def b_call(self,channel):
        self.b_ticks += 1
        self.tot_call() 
    
    def get_ticks(self):
        
        return self.tot_ticks
    
    def get_a_ticks(self):
        return self.a_ticks
    
    def get_b_ticks(self):
        return self.b_ticks
    
    def reset(self):
        self.a_ticks, self.b_ticks, self.tot_ticks = 0, 0, 0
        
        
        
        
