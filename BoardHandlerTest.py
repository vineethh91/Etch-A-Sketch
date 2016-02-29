#!/usr/bin/env python2.7

from BoardHandler import BoardHandler

class BoardHandlerTest:
 
    # Test User initiatied board initialization
    def initializeBoardTest(self):
        print "Testing BoardHandler initiazilation"
        board = BoardHandler()
        board.initializeBoard()


boardHandlerTest = BoardHandlerTest() 
boardHandlerTest.initializeBoardTest()
