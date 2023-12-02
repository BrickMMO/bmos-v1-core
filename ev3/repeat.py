#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Button, Color
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()

def execute():

  ev3.speaker.set_volume(10)
  ev3.speaker.say("CHANGE ONE")

  