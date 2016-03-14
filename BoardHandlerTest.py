#!/usr/bin/env python2.7

from BoardHandler import BoardHandler
from ImageBufferCreator import ImageBufferCreator 
import numpy as npy 
import BasicMappings as MAP 
import time

class BoardHandlerTest:
 
    board = None 
    imageBufferCreator = None 

    characterMaplist = [MAP.A, MAP.B, MAP.C, MAP.D]

    # Test User initiatied board initialization
    def initializeBoardTest(self):
        print "Testing BoardHandler initiazilation"
        self.board = BoardHandler()
        self.imageBufferCreator = ImageBufferCreator()
        self.board.initializeBoard()
        self.board.initializePins()

    def getBufferWithFill(self, fill):
        # initialize entire 32x32x3 matrix to all 1s for a white background 
        return [[[fill for k in xrange(3)] for j in range(32)] for i in range(32)]
        
    def getBufferWithRGBBackground(self, r, g, b):
        # initialize entire 32x32x3 matrix to r/g/b background 
        return [[[r, g, b] for j in range(32)] for i in range(32)]

    # outputBuffer = destination
    # inputBuffer = source
    # color = list of R/G/B eg. [1,0,0]
    # offset = lines to offset counting from 0
    def copyToOutputBuffer(self, outputBuffer, inputBuffer, color, offset):
      for i in range(len(inputBuffer)):
        for j in range(32):
          if(inputBuffer[i][j] != 0): 
            outputBuffer[i + offset][j] = color 

      return outputBuffer

    def printString(self):
        print "Printing various strings to Board"

        concatenatedString = self.imageBufferCreator.convertStringToBuffer("h e l lo        wor l d !        ")
        secondString = self.imageBufferCreator.convertStringToBuffer("p oopd ic k    ")
        
        loopCounts = 0
        while (loopCounts < 100):
          loopCounts += 1 

          # reset buffer to blank image so we dont overwrite
          buffer = self.getBufferWithFill(0)
 
          # copy the string buffer to print-able buffer
          buffer = self.copyToOutputBuffer(buffer, concatenatedString, [0,1,0], 0)
          buffer = self.copyToOutputBuffer(buffer, secondString, [0,0,1], 16)

          # print to buffer
          self.board.printBufferToBoard(buffer)

          # roll the entire matrix in opposite directions by one column
          concatenatedString = npy.roll(concatenatedString, -1, axis = 1)
          secondString = npy.roll(secondString, 1, axis = 1)
 
          # let me sleep goddamn you, doing all this work is tiring 
          time.sleep(0.005)


    def printLetters(self):
        print "Printing Letters of various sizes to Board 1x, 2x, 3x & 4x"
        index = 0

        for i in range(1,5):
          # kronecker product to scale the matrix for the various size(scale factor of 8x)
          scaledA = npy.kron(self.characterMaplist[index], npy.ones((i,i)))
          buffer = self.getBufferWithFill(0)
          for k in range(8*i):
            for j in range(8*i):
              if(scaledA[k][j] != 0):
                buffer[k][j] = [0,1,0] 
          for z in range(40):
            self.board.printBufferToBoard(buffer)

    def testDifferentDiagnostics(self):

        print "Printing diamond shape to Board that will scroll left on a loop" 

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

        loopCounts = 0
        while (loopCounts < 100):
          loopCounts += 1 

          self.board.printBufferToBoard(buffer)
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

        loopCounts = 0
        while (loopCounts < 100):
          loopCounts += 1 

          board.printBufferToBoard(buffer)


boardHandlerTest = BoardHandlerTest() 
boardHandlerTest.initializeBoardTest()
boardHandlerTest.printString()
boardHandlerTest.printLetters()
boardHandlerTest.testDifferentDiagnostics()
boardHandlerTest.drawShapes()
