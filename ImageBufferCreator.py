#!/usr/bin/env python2.7

# References for drawing - https://github.com/adafruit/rpi-rgb-led-matrix/blob/master/matrixtest2.py
# ImageDraw - http://effbot.org/imagingbook/imagedraw.htm

from PIL import Image
from PIL import ImageDraw
import time
import numpy as npy
import BasicMappings as Map

class ImageBufferCreator: 

    image = Image.new("1", (32, 32))

    matrixMap = { 'a' : Map.A,
                  'b' : Map.B,
                  'c' : Map.C,
                  'd' : Map.D,
                  'e' : Map.E,
                  'h' : Map.H,
                  'i' : Map.I,
                  'k' : Map.K,
                  'l' : Map.L,
                  'o' : Map.O,
                  'p' : Map.P,
                  'r' : Map.R,
                  'w' : Map.W,
                  # special characters
                  '!' : Map.Exclamation,
                  ' ' : Map.E_S
                  
                }


    def __init__(self):
        print "ImageBufferCreator Constructor"
        self.resetImage()

    def resetImage(self):
        image = Image.new("1", (32, 32))
        
    def getImage(self):
        return self.image

    def getImageAsArray(self):
        return npy.array(self.image.getdata(), dtype=npy.uint8).reshape(32,32)

    def printImageArray(self):
        arr = self.getImageAsArray()
        for i in range(32):
            print arr[i]

    def drawLines(self, x0, y0, x1, y1):
        draw  = ImageDraw.Draw(self.image) 
        draw.line((x0, y0, x1, y1), fill=1)

        return self.image

    def drawRectangle(self, x0, y0, x1, y1):
        draw  = ImageDraw.Draw(self.image) 
        draw.rectangle((x0, y0, x1, y1), fill=0, outline=1)

        return self.image

    def rotateImage(self, angle):
        self.image = self.image.rotate(angle)

    # Takes in a string to convert to a image buffer to be drawn onto the board
    def convertStringToBuffer(self, stringToBePrinted):
         stringBuffer = self.matrixMap.get(" ")
         for character in stringToBePrinted:
           stringBuffer = npy.hstack((stringBuffer, self.matrixMap.get(character, self.matrixMap.get(" "))))

         return stringBuffer


