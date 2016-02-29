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

# Pin initializations based on above mapping
R0 = 7
G0 = 11
B0 = 13
R1 = 15
G1 = 19
B1 = 21
A  = 23
B  = 29
C  = 31
D  = 33
CLK = 35
STB = 37
OE = 40

SLEEP_TIME_BETWEEN_ROWS = 0.1
SLEEP_TIME_BETWEEN_LED_SHIFT = 0.05

INITIALIZATION_LOOP_COUNT = 48 # 16 rows x 3 times each = 48 

class BoardHandler :


    def __init__(self):
        print "BoardHandler Constructor"
        GPIO.setwarnings(False)

    def cleanUpBoard(self):
        GPIO.cleanup()

    # Kick off initialization packets to the Board to boot up
    # Cycles through all the rows + all colours of each LED so you can visually ensure everything is wired up and working correctly
    def initializeBoard(self):
        print "Initializing Board..."
        self.initializePins()

        row = 0
        column = 1 
        loopCount = INITIALIZATION_LOOP_COUNT
        while loopCount >= 0:
          loopCount -= 1 
          for i in range(0,31):

            red = False
            blue = False
            green = False
            if(column == 1):
              red = True
            elif(column == 2):
              green = True
            else:
              blue = True

            GPIO.output(R0, red) 
            GPIO.output(G0, green) 
            GPIO.output(B0, blue) 

            GPIO.output(R1, red) 
            GPIO.output(G1, green) 
            GPIO.output(B1, blue) 
            column += 1
            if(column > 3):
              column = 1

            self.setDemuxRowPinValues(row)

            self.clockData()

            self.enableStrobe()

          # finished shifting in all 32 columns, moving to the next row
          row += 1
          # if row > 15 then reset back to 0 to loop back to the start
          if(row > 15):
            row = 0
          time.sleep(SLEEP_TIME_BETWEEN_ROWS)

        print "Initialization done done done"
 

    # Initialize pins to BOARD pin references & pin-out, set OE/CLK/STB to LOW
    # OE = LOW implies is deasserted which means the row will be turned ON 
    #    = HIGH implies its asserted and turns the row OFF
    def initializePins(self):
        # GPIO.Board tells it to use the Board pin numbers and NOT the GPIO pin numbers, GPIO.BCM would set it to reference GPIO numbers
        GPIO.setmode(GPIO.BOARD);
        GPIO.setup(R0, GPIO.OUT);
        GPIO.setup(G0, GPIO.OUT);
        GPIO.setup(B0, GPIO.OUT);
        GPIO.setup(R1, GPIO.OUT);
        GPIO.setup(G1, GPIO.OUT);
        GPIO.setup(B1, GPIO.OUT);
        GPIO.setup(A, GPIO.OUT);
        GPIO.setup(B, GPIO.OUT);
        GPIO.setup(C, GPIO.OUT);
        GPIO.setup(D, GPIO.OUT);
        GPIO.setup(CLK, GPIO.OUT);
        GPIO.setup(STB, GPIO.OUT);
        GPIO.setup(OE, GPIO.OUT);

        # Set everything to low initially
        # We may need to set OE to HIGH so we only make the data visible once everything has been latched and then strobed onto the output registers
        GPIO.output(OE, GPIO.LOW)
        GPIO.output(CLK, GPIO.LOW)
        GPIO.output(STB, GPIO.LOW)

    # Trigger clock once all bits are ready on the lines
    # Clocks it into the internal latches on the LED Matrix board
    def clockData(self):
        GPIO.output(CLK, GPIO.HIGH)
        # Sleep shouldnt be needed unless you want to slow down to debug
        #time.sleep(0.01)
        GPIO.output(CLK, GPIO.LOW)

    # Enabling strobe for a single clock cycle pushes everything currently latched internally onto the output register making it visible 
    def enableStrobe(self):
        GPIO.output(STB, GPIO.HIGH)
        # Sleep shouldnt be needed unless you want to slow down to debug
        #time.sleep(0.05)
        GPIO.output(STB, GPIO.LOW)

    # Takes the current row thats being shifted and sets the pins for the demux-er to interpret the rows being shifted into
    # A[3:1] <-- where highest bit is D pin and lowest bit is A pin
    def setDemuxRowPinValues(self, row):
        # demux pins to reference rows
        aPin = True if (row & 1 != 0) else False
        bPin = True if (row & 2 != 0) else False 
        cPin = True if (row & 4 != 0) else False 
        dPin = True if (row & 8 != 0) else False 

        print "Shifting data for row " , row , "Binary representation => ", bin(row).zfill(4), dPin, cPin, bPin, aPin

        GPIO.output(A,aPin) 
        GPIO.output(B,bPin) 
        GPIO.output(C,cPin) 
        GPIO.output(D,dPin) 
    
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
