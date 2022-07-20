import RPi.GPIO as GPIO
import sys
import time

# exit on no args
if (len(sys.argv) != 2):
    print('please add a command')

pcPowerPin = 3
pcResetPin = 5

# read script arguments
arg = sys.argv[1]

####    
# functions
####    

def configureGPIO():
    # configuring general GPIO pins
    GPIO.setwarnings(False) # disable output
    GPIO.setmode(GPIO.BOARD) # enable pin numbering like board

    # configuring single GPIO pins
    GPIO.setup(pcPowerPin, GPIO.OUT) # output pin
    GPIO.output(pcPowerPin, GPIO.LOW) # power off
    GPIO.setup(pcResetPin, GPIO.OUT) # output pin
    GPIO.output(pcResetPin, GPIO.LOW) # power off

def activateRelais(pin, sec = .5):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(sec)
    GPIO.output(pin, GPIO.LOW)

def exitSave(mode):
    GPIO.cleanup()
    sys.exit(mode)

####    
# script
####
configureGPIO()

if (arg == 'reset'):
    activateRelais(pcResetPin)
elif (arg == 'power'):
    activateRelais(pcPowerPin)
elif (arg == 'powerhard'):
    activateRelais(pcPowerPin, 5)
else:
    print('Unknown command')
    exitSave(1)

exitSave(0)