#!/usr/bin/env python2.7

from BoardHandler import BoardHandler
from ImageBufferCreator import ImageBufferCreator 
import numpy as npy 

class BoardHandlerTest:
 
    # Test User initiatied board initialization
    def initializeBoardTest(self):
        print "Testing BoardHandler initiazilation"
        board = BoardHandler()
        board.initializeBoard()

    def getBufferWithFill(self, fill):
        # initialize entire 32x32x3 matrix to all 1s for a white background 
        return [[[fill for k in xrange(3)] for j in range(32)] for i in range(32)]
        
    def getBufferWithRGBBackground(self, r, g, b):
        # initialize entire 32x32x3 matrix to r/g/b background 
        return [[[r, g, b] for j in range(32)] for i in range(32)]

    def testDifferentDiagnostics(self):
        print "Printing Buffer to Board"
        board = BoardHandler()
        board.initializeBoard()
        board.initializePins()

        buffer = self.getBufferWithFill(0)
        #buffer = self.getBufferWithRGBBackground(0,1,0)
        j = 15
        redColour   = [1,0,0]
        greenColour = [0,1,0]
        blueColour  = [0,0,1]
        for i in range(16):
            buffer[i][j] = redColour 
            buffer[31-i][j] = redColour 

            buffer[i][31-j] = redColour 
            buffer[31-i][31-j] = redColour 
            j -= 1

        count = 2000
        while True:
            board.printBufferToBoard(buffer)
            buffer = npy.roll(buffer, -1, axis = 1)

    def drawShapes(self):
        board = BoardHandler()
        board.initializePins()

        # Create drawer buffer and draw an X on the buffer
        bufferCreator = ImageBufferCreator()
        bufferCreator.drawLines(0,0,31,31)
        bufferCreator.drawLines(0,31,31,0)
        
        # Prints array to STDOUT 
        bufferCreator.printImageArray()

        # Rotates the X by 45 degrees making it a + sign
        bufferCreator.rotateImage(45)

        buffer = self.getBufferWithFill(0)
        arr = bufferCreator.getImageAsArray()

        for i in range(32):
            for j in range(32):
                if(arr[i][j] != 0):
                    buffer[i][j] = [1,0,0] 
        while True:
            board.printBufferToBoard(buffer)

boardHandlerTest = BoardHandlerTest() 
boardHandlerTest.testDifferentDiagnostics()
boardHandlerTest.drawShapes()
