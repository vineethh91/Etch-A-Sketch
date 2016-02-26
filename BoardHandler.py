#!/usr/bin/env python2.7

# BoardHandler handles all functions related to board interactions
#  *Initialize board/boot up sequence(s)
#  *Diagnostics 
#  *Send/Get image

# For the below reference RP2_Pingout.png
#
# Panel Pin     RPi 	Notes
# R0	1	7 	GPIO4
# G0	2	11 	GPIO17
# B0	3	13	GPIO27
# GND	4	9	GND
# R1	5	15	GPIO22
# G1	6	19	GPIO10
# B1	7	21	GPIO09
# GND	8	25	GND
# A	9	23	GPIO11
# B	10	29	GPIO5
# C	11	31	GPIO6
# D	12	33	GPIO13
# CLK	13	35	GPIO19
# STB	14	37	GPIO26
# OE	15	40	GPIO21
# GND	16	39	GND



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
