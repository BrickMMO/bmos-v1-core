#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from sys import exit

import os
import time

import urequests as requests
import ujson as json


def updateEnv():

    try:
        f = open(".env", "r")
    except:
        print(".en file does not exist")
        exit()

    for line in f:

        data = line.split('=')

        if len(data) > 1:

            # print("global " + str(data[0]) + " = \"" + str(data[1]).strip() + "\"")
            exec("global " + str(data[0]))
            exec("" + str(data[0]) + " = \"" + str(data[1]).strip() + "\"")

    try:
        GITHUB_ACCESS_TOKEN
    except:
        print("GITHUB_ACCESS_TOKEN variable does not exist")
        exit()

def updateConfig():

    try:
        f = open(".config", "r")
    except:
        print(".en file does not exist")
        exit()

    for line in f:

        data = line.split('=')

        if len(data) > 1:

            # print("global "  + str(data[0]) + " = \"" + str(data[1]).strip() + "\"")
            exec("global " + str(data[0]))
            exec("" + str(data[0]) + " = \"" + str(data[1]).strip() + "\"")

    try:
        LAST_UPDATE
    except:
        print("LAST_UPDATE variable does not exist")
        exit()


def getLastUpdate():

    url = 'https://api.github.com/repos/BrickMMO/bmos'

    headers = {
        'Authorization': 'Bearer ' + GITHUB_ACCESS_TOKEN,
        'Content-Type': 'application/json',
        'User-Agent' : 'BMOS'
    }

    response = requests.get(url, headers = headers)

    response = json.loads(response.text)

    # print(response)
    # print(response['pushed_at'])

    pushed_at = response['pushed_at']   
    # print(pushed_at)

    year = pushed_at[0:4]
    month = pushed_at[5:7]
    day = pushed_at[8:10]
    hours = pushed_at[11:13]
    minutes = pushed_at[14:16]
    seconds = pushed_at[17:19]

    # print(year)
    # print(month)
    # print(day)
    # print(hours)
    # print(minutes)
    # print(seconds)

    global LAST_PUSH
    LAST_PUSH = str(year) + str(month) + str(day) + str(hours) + str(minutes) + str(seconds)

    # print(LAST_PUSH)

def update_repeat():

    f = open(".config", "w")
    f.write("LAST_UPDATE=" + LAST_PUSH)

    url = 'https://raw.githubusercontent.com/BrickMMO/bmos/main/ev3/repeat.py'

    headers = {
        'Authorization': 'Bearer ' + GITHUB_ACCESS_TOKEN,
        'Content-Type': 'application/json',
        'User-Agent' : 'BMOS'
    }

    response = requests.get(url, headers = headers)
    response = response.text

    f = open("bmos" + LAST_PUSH + ".py", "w")
    f.write(response)



while True:

    updateEnv()
    updateConfig()

    getLastUpdate()

    if(LAST_PUSH > LAST_UPDATE):

        print("Update requried")
        
        updateRepeat()
        
    else:

        print("No update requried")

    print("Waiting 10 seconds")
    time.sleep(10)


print("DONE")



exit()

try: 
    f = open("bmos" + str(LAST_UPDATE) + ".py", "r")
except:
    print("BMOS file does not exist")
    exit()



'''
while True:

    time.sleep(10)

    print("Looping!")
'''