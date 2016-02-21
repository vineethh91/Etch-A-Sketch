#!/usr/bin/env python2.7

# BoardHandler handles all functions related to board interactions
#  *Initialize board/boot up sequence(s)
#  *Diagnostics 
#  *Send/Get image

import RPi.GPIO as GPIO
import time

# Using for debugging purposes
TEST_PIN = 7

class BoardHandler :


    def __init__(self):
        print "BoardHandler Constructor"
        GPIO.setwarnings(False)

    # Kick off initialization packets to the Board to boot up
    def initializeBoard(self):
        print "Initializing Board..."
        GPIO.setmode(GPIO.BOARD);
        GPIO.setup(TEST_PIN, GPIO.OUT);
        for i in range(0,5):
            print "Flipping debug LED on pin ", TEST_PIN
            GPIO.output(TEST_PIN, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(TEST_PIN, GPIO.LOW)
            time.sleep(0.5)
        print "Something better have blinked"
        GPIO.cleanup()
 

    # Diagnostics
    # Invoked to do a complete board diagnostics(every pixel working?, 
    # known patterns continue to print? = useful for debugging)
    #
    # @timer - duration in milliseconds for how long the diagnostics should run
    def startBoardDiagnostics(self, timer):
        print "Starting Board diagnostics..."


    def updateBoard(self):
        print "Sending next buffer to Board..."

    def getCurrentImageOnBoard(self): 
        print "Returning current buffer to requester..."
