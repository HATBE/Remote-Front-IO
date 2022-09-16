import RPi.GPIO as GPIO
from os.path import exists
import time
import json

outputJsonFile = '/var/www/html/web/pcState.json'
state = 0
oldState = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.IN)

def initWrite():
    with open(outputJsonFile, 'w') as wFile:
        json.dump({"state": state, "date": round(time.time())}, wFile)

if(not exists(outputJsonFile)):
    initWrite()
else:
    try:
        with open(outputJsonFile, 'r') as rFile:
            if(not json.load(rFile)):
                None
    except:
        initWrite()

while True:
    time.sleep(1)

    with open(outputJsonFile, 'r') as rFile:
        jsonR = json.load(rFile)
        if("state" in jsonR):
            oldState = jsonR['state']

    state = GPIO.input(16)

    if(state == oldState):
        continue

    with open(outputJsonFile, 'w') as wFile:
        json.dump({"state": state, "date": round(time.time())}, wFile)