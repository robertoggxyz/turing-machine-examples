# -*- coding: utf-8 -*-
"""
MIT License

Copyright (c) 2019 robertoggxyz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os, time

RIGHT = 'r'
LEFT  = 'l'
BLANK = '_'

# The quintuple defines a complete state of the machine
class Quintuple:
    # Original arg names in the book (p, x, y, dir, q)
    def __init__(self, inState, inSymbol, outSymbol, headDirection, outState):
        self.inState = inState
        self.inSymbol = inSymbol
        self.outSymbol = outSymbol
        self.headDirection = headDirection
        self.outState = outState

# The Turing machine works with an array of quintuples
class TuringMachine:
    def __init__(self, quintuples, initialState, haltStates):
        self.quintuples = quintuples
        self.initialState = initialState
        self.haltStates = haltStates
        
    def run(self, tape, initPos):
        self.tape = tape
        self.halt = False
        self.currentPos = initPos
        self.currentState = self.initialState
        while(not self.halt):
            self.step()
            
    def step(self):
        self.printMachine()
        time.sleep(1)
        if self.halt == False:
            self.evaluate()
        else:
            self.halt = True
        self.printMachine()
        time.sleep(1)                 
            
    def evaluate(self):
        for i in range(len(self.quintuples)):
            if(self.quintuples[i].inState == self.currentState and
               self.quintuples[i].inSymbol == self.tape[self.currentPos]):
                self.tape[self.currentPos] = self.quintuples[i].outSymbol
                self.currentState = self.quintuples[i].outState
                if self.currentState in self.haltStates:
                    self.halt = True
                elif self.quintuples[i].headDirection == RIGHT:                    
                    self.currentPos += 1
                    break
                else:                    
                    self.currentPos -= 1
                    break        
                
    def printMachine(self):
        if os.name == 'nt':
            os.system('cls')
        else: # assuming unix family
            os.system('clear')
        print('                                      state: ', self.currentState)
        print('                                       halt: ', self.halt)
        print('                        |           headPos: ', self.currentPos)
        print('                       \|/')
        strValues = ''
        for i in range(len(self.tape)):
            strValues += str(self.tape[i])
            strValues += ' '        
        offset = '                       '
        i = self.currentPos
        while i > 0:
            offset = offset[:len(offset) - 2]
            i -= 1
        print(offset, strValues)
        
