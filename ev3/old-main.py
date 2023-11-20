#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

'''
import urequests as requests
'''

import test

# import os
# import subprocess
import uos
import os

import time





# Print all available modules
# help('modules')

'''
headers = {
    'Authorization': 'Bearer ' + API_KEY,
    'Content-Type': 'application/json'
}

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

now = time.time()
now = str(now)

f = open("/home/robot/ev3/" + now, "a")
f.write(now)
f.close()
'''

# Create your objects here.
ev3 = EV3Brick()

'''
while True:
    # res = requests.get(url='http://www.baidu.com/')
    # print(res.text)
    print("Working!")
    time.sleep(3)
    ev3.speaker.beep()
'''

# Write your program here.
ev3.speaker.beep()

time.sleep(1)

ev3.speaker.say("Restarting")

# /usr/bin/brickrun --directory="/home/robot/ev3" "/home/robot/ev3/main.py"


# os.system('bash bmos.sh')

# result = subprocess.run(['bash', './test.sh'])

# result = uos.system('ls -l')
# result = uos.system('bash bmos.sh')
# print(result)


'''
import os

filepath = "\home\robot\ev3\bmos.sh"
process_id = os.spawnv(os.P_NOWAIT , filepath , ["-someFlag" , "someOtherFlag"])
print(process_id)
'''


test.execute()
test.execute()






f = open("/home/robot/ev3/next.py", "a")
f.write('''import time

def execute():

  now = time.time()
  now = str(now)

  f = open(\"/home/robot/ev3/tmp/n-" + now, "a")
  f.write(now)
  f.close()''')
f.close()

import next

next.execute()
