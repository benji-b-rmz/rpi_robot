#Benjamin Ramirez
#August 4, 2016
#testing out the ranger class from ultrasonic_rangers.py

import time
from sensors import rangers

#initializing the ranger object with the pins
back_left_sensor = rangers.ranger(17,4)

for x in range(10):
    time.sleep(0.5)
    print back_left_sensor.get_dist()
