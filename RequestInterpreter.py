#!/usr/bin/env python2.7

# Invoked from the webserserver to interpret the incoming request
# Supposed input will be array of key:value pairs 
#   eg. "command:updateBoard"
#       "duration:5000"
#       "command:startDiagnostics"
#

from BoardHandler import BoardHandler

class RequestInterpreter:

 
    # Interpret incoming request to kick off action handlers based on request
    def interpretRequest(self):
        print "RequestInterpreter interpretRequest invoked..."
 
    # User initiatied board initialization
    def initializeBoard(self):
        print "Invoking BoardHandler to initialize as per user request..."
        board = BoardHandler()
        board.initializeBoard()

    # Saves the incoming request data to local buffer 
    # Can be used if user only wants to queue up their request
    def saveData(self):
        print "Saving request data to buffer..."

    # Kick off transmitting data to the board/external output
    def displayData(self): 
        print "Invoking BoardHandler to display data..."


request = RequestInterpreter()
request.initializeBoard()


