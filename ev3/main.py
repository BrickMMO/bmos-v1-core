#!/usr/bin/env pybricks-micropython
from sys import exit

import os, time

import urequests as requests
import ujson as json


'''
This function opens the .env file and creates global variables for 
each line in the .env file. 
'''

def updateEnv():

    try:
        f = open(".env", "r")
    except:
        print(".env file does not exist")
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

'''
This function opens the .config file and creates global variables for 
each line in the .config file. 
'''

def updateConfig():

    try:
        f = open(".config", "r")
    except:
        print(".config file does not exist")
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

'''
This function checks the bmos-v1-core repo for the last update and sets a 
global variable.
'''

def getLastUpdate():

    url = 'https://api.github.com/repos/BrickMMO/bmos-v1-core'

    headers = {
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Expires': '0',
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

'''
This function will download the newest 
'''

def updateRepeat():

    f = open(".config", "w")
    f.write("LAST_UPDATE=" + LAST_PUSH)

    url = 'https://raw.githubusercontent.com/BrickMMO/bmos-v1-core/main/ev3/repeat.py?last=' + LAST_PUSH

    headers = {
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Expires': '0',
        'Authorization': 'Bearer ' + GITHUB_ACCESS_TOKEN,
        'Content-Type': 'application/json',
        'User-Agent' : 'BMOS'
    }

    response = requests.get(url, headers = headers)
    response = response.text

    print(response)

    f = open("bmos" + LAST_PUSH + ".py", "w")
    f.write(response)


counter = 0

while True:

    updateEnv()
    updateConfig()

    getLastUpdate()

    if(LAST_PUSH > LAST_UPDATE):

        print("Update requried")
        
        updateRepeat()
        
    else:

        print("No update requried")

    exec("import bmos" + LAST_PUSH)
    exec("bmos" + LAST_PUSH + ".execute()")

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