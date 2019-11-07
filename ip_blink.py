#!/usr/bin/env python
# Ref: http://www.esologic.com/blink-out-ip-address-for-raspberry-pi-using-python/
# 

import RPi.GPIO as GPIO ## Import GPIO library

import time
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering

led = 35
button=29
GPIO.setup(led, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button

from subprocess import *

while True:
  input_state=GPIO.input(button)

  # Wait for the button to be pushed without maxing out the CPU
  GPIO.wait_for_edge(button, GPIO.FALLING) 

  if (GPIO.input(button) == False):
    ip = Popen("ip -4 addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1", shell=True, stdout=PIPE).communicate()[0]
    print ip

    for x in range(3): #three long blinks to indicate procedure is starting

        GPIO.output(led,True)
        time.sleep(.4)
        GPIO.output(led,False)
        time.sleep(.4)

    time.sleep(5) # followed by a delay

    print "starting" 

    for x in list(ip):

        time.sleep(2)
        print x

        if x.isdigit():
            if (int(x) == 0):
                # long LED light indicating zero
                GPIO.output(led,True)
                time.sleep(3)
                GPIO.output(led,False)

            elif (int(x) != 0):
                for y in range(int(x)):

                    GPIO.output(led,True)
                    time.sleep(.5)
                    GPIO.output(led,False)
                    time.sleep(.5)

        elif (x == '.'):
            for x in range(6): #six rapid blinks indicate a .

                GPIO.output(led,True)
                time.sleep(.1)
                GPIO.output(led,False)
                time.sleep(.1)

            time.sleep(2)
