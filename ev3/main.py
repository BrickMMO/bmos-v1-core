#!/usr/bin/env pybricks-micropython
from sys import exit

import os, time

import urequests as requests
import ujson as json

import env
import config
import github

# Use env variable to cinfigure GitHub
github.set_token(env.get('GITHUB_ACCESS_TOKEN'))

if config.get('LAST_UPDATE') == False:

    config.set('LAST_UPDATE', '000')


'''
This is the main loop that controls what happens when
'''

def update_repeat():


    last_push = github.repo_last_push('BrickMMO', 'bmos-v1-core')

    if(last_push > config.get('LAST_UPDATE')):

        print('NOTICE: Update needed')

        repeat = github.fetch_file('BrickMMO', 'bmos-v1-core', 'main', 'ev3/repeat.py')

        config.set('LAST_UPDATE', last_push)

        f = open("bmos" + config.get('LAST_UPDATE') + ".py", "w")
        f.write(repeat)
        f.close()

    else:

        print('NOTICE: No update needed')


while True:

    update_repeat()

    if config.get('ID') == '':

        print('IM HERE')

    print('Notice: Import bmos' + config.get('LAST_UPDATE'))

    exec("import bmos" + config.get('LAST_UPDATE'))
    exec("bmos" + config.get('LAST_UPDATE') + ".execute()")

    print("Waiting 10 seconds")
    time.sleep(10)


print("DONE")
