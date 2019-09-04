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

from turing_machine import TuringMachine
from turing_machine import Quintuple
from turing_machine import RIGHT
from turing_machine import LEFT
from turing_machine import BLANK

# Testing a machine to increment the nonnegative decimal input in 1
def testDecimalSuccessorMachine(tape, initPos):
    # Machine quintuples
    q1 = Quintuple('s', 0, 0, RIGHT, 's') # In state s, it moves to RHE, the right-hand-end
    q2 = Quintuple('s', 1, 1, RIGHT, 's') # of the string of nonblank symbols
    q3 = Quintuple('s', 2, 2, RIGHT, 's')
    q4 = Quintuple('s', 3, 3, RIGHT, 's')
    q5 = Quintuple('s', 4, 4, RIGHT, 's')
    q6 = Quintuple('s', 5, 5, RIGHT, 's')
    q7 = Quintuple('s', 6, 6, RIGHT, 's')
    q8 = Quintuple('s', 7, 7, RIGHT, 's')
    q9 = Quintuple('s', 8, 8, RIGHT, 's')
    q10 = Quintuple('s', 9, 9, RIGHT, 's')
    q11 = Quintuple('s', BLANK, BLANK, LEFT, 't') # When it goes past the RHE, it steps left
                                                  # and goes to state t 
    
    q12 = Quintuple('t', 0, 1, LEFT, 'h') # In state t, it adds 1 to current digit and halts
    q13 = Quintuple('t', 1, 2, LEFT, 'h')
    q14 = Quintuple('t', 2, 3, LEFT, 'h')
    q15 = Quintuple('t', 3, 4, LEFT, 'h')
    q16 = Quintuple('t', 4, 5, LEFT, 'h')
    q17 = Quintuple('t', 5, 6, LEFT, 'h')
    q18 = Quintuple('t', 6, 7, LEFT, 'h')
    q19 = Quintuple('t', 7, 8, LEFT, 'h')
    q20 = Quintuple('t', 8, 9, LEFT, 'h')
    q21 = Quintuple('t', 9, 0, LEFT, 't') # But if the current digit is 9, it "carries one"
    q22 = Quintuple('t', BLANK, 1, LEFT, 'h') # for when the input is all 9's
    
    quintuples = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14,
                  q15, q16, q17, q18, q19, q20, q21, q22]
    
    tapeCopy = tape.copy()
    machine = TuringMachine(quintuples, 's', ['h'])
    machine.run(tape, initPos)
    print('Decimal succesor machine, input was: ', tapeCopy, '\n')
    
# Testing a machine to check palindromes with {a, b} alphabet
def testPalindromeMachine(tape, initPos):
    # Machine quintuples
    q1 = Quintuple('s', 'a', BLANK, RIGHT, '1') # In state s, it scans the LHE, the left-hand-end.
                                                # If w starts with an 'a', does it end in an 'a'?
    
    q2 = Quintuple('1', 'a', 'a', RIGHT, '1') # In state 1, it moves to RHE
    q3 = Quintuple('1', 'b', 'b', RIGHT, '1')
    q4 = Quintuple('1', BLANK, BLANK, LEFT, '2') # and goes to state 2
    
    q5 = Quintuple('2', 'a', BLANK, LEFT, '3') # In state 2, it checks that RHE = 'a'
    q6 = Quintuple('2', 'b', 'b', RIGHT, 'no')
    q7 = Quintuple('2', BLANK, BLANK, LEFT, 'yes') # was w = 'a'? [or was X = 'a'?]
    
    q8 = Quintuple('3', 'a', 'a', LEFT, '3') # In state 3, it moves back to LHE
    q9 = Quintuple('3', 'b', 'b', LEFT, '3')
    q10 = Quintuple('3', BLANK, BLANK, RIGHT, 's') # and starts again
    
    q11 = Quintuple('s', 'b', BLANK, RIGHT, '4') # If w starts with a 'b', does it end in a 'b'?
    
    q12 = Quintuple('4', 'a', 'a', RIGHT, '4') # In state 4, it moves to RHE
    q13 = Quintuple('4', 'b', 'b', RIGHT, '4')
    q14 = Quintuple('4', BLANK, BLANK, LEFT, '5')
    
    q15 = Quintuple('5', 'a', 'a', RIGHT, 'no') # In state 5, it checks that RHE = 'b'
    q16 = Quintuple('5', 'b', BLANK, LEFT, '3')
    q17 = Quintuple('5', BLANK, BLANK, LEFT, 'yes') # was w = 'b'? [or was X = 'b'?]
    
    q18 = Quintuple('s', BLANK, BLANK, RIGHT, 'yes') # Is the word with no letters a palindrome?
    
    quintuples = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14,
                  q15, q16, q17, q18]
    
    tapeCopy = tape.copy()
    machine = TuringMachine(quintuples, 's', ['yes', 'no'])
    machine.run(tape, initPos)
    print('Palindrome machine, input was: ', tapeCopy, ', if palyndrome then state = yes\n')
    
# Testing a machine to add binary values
def testBinaryAdderMachine(tape, initPos):
    # Machine quintuples
    q1 = Quintuple('s', 0, 0, RIGHT, 's') # In state s, it moves to RHE
    q2 = Quintuple('s', 1, 1, RIGHT, 's')
    q3 = Quintuple('s', 'a', 'a', RIGHT, 's') # Latter, there will be a's and b's in the summand
    q4 = Quintuple('s', 'b', 'b', RIGHT, 's')
    q5 = Quintuple('s', '+', '+', RIGHT, 's')
    q6 = Quintuple('s', BLANK, BLANK, LEFT, '1')
    
    q7 = Quintuple('1', 0, BLANK, LEFT, '2') # In state 1, it finds x = 0
                                             # We'll do the other cases for x later
    
    q8 = Quintuple('2', 0, 0, LEFT, '2') # In state 2, it moves left across 0 and 1 to +
    q9 = Quintuple('2', 1, 1, LEFT, '2')
    q10 = Quintuple('2', '+', '+', LEFT, '3')
    
    q11 = Quintuple('3', 'a', 'a', LEFT, '3') # In state 3, it moves left across a and b to y
    q12 = Quintuple('3', 'b', 'b', LEFT, '3')
    q13 = Quintuple('3', 0, 'a', RIGHT, 's') # y = 0, and x + y = 0, but this is recorded as a
                                             # Then, we move right to get the next x
    
    q14 = Quintuple('3', BLANK, 'a', RIGHT, 's') # When there is no corresponding bit y because the
                                                 # summand is shorter than the addend, we take 0 for
                                                 # y and record an a and move right to get the next x
    
    q15 = Quintuple('3', 1, 'b', RIGHT, 's') # y = 1 and x + y = 1, but this is recorded as b
                                             # Then, we move right to get the next x
    
    q16 = Quintuple('1', 1, BLANK, LEFT, '4') # In state 1, it finds x = 1
    
    q17 = Quintuple('4', 0, 0, LEFT, '4') # In state 4, it move left across 0 and 1 to +
    q18 = Quintuple('4', 1, 1, LEFT, '4')
    q19 = Quintuple('4', '+', '+', LEFT, '5')
    
    q20 = Quintuple('5', 'a', 'a', LEFT, '5') # In state 5, it moves left across a and b to y
    q21 = Quintuple('5', 'b', 'b', LEFT, '5')
    q22 = Quintuple('5', '0', 'b', RIGHT, 's') # y = 0 and x + y = 1, but this is recorded as b
                                               # Then, we move right to get the next x
    
    q23 = Quintuple('5', BLANK, 'b', RIGHT, 's') # When there is no corresponding bit y, take 0 for y
                                                 # and record a 'b' and move right to get the next x
    
    q24 = Quintuple('5', 1, 'a', LEFT, '6') # y = 1 and x + y = 10, but this is recorded as a
                                            # Then, we move to state 6 and carry the one
    
    q25 = Quintuple('6', 0, 1, RIGHT, 's')
    q26 = Quintuple('6', BLANK, 1, RIGHT, 's')
    q27 = Quintuple('6', 1, 0, LEFT, '6')
    
    q28 = Quintuple('1', '+', BLANK, LEFT, '7') # In state 1, it finds no x
    
    q29 = Quintuple('7', 'a', 0, LEFT, '7') # In state 7, it replaces a's by 0s
    q30 = Quintuple('7', 'b', 1, LEFT, '7') # and it replaces b's by 1s
    q31 = Quintuple('7', 0, 0, LEFT, '7')   # moves to the LHE
    q32 = Quintuple('7', 1, 1, LEFT, '7')
    q33 = Quintuple('7', BLANK, BLANK, RIGHT, 'h') # and halts
    
    quintuples = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14,
                  q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26,
                  q27, q28, q29, q30, q31, q32, q33]
    
    tapeCopy = tape.copy()
    machine = TuringMachine(quintuples, 's', ['h'])
    machine.run(tape, initPos)
    print('Binary adder machine, input was: ', tapeCopy, '\n')
                
if __name__ == '__main__':
    while(True):
        print('Testing Turing machines, select one option:')
        print('  1: Decimal successor machine')
        print('  2: Palindrome machine with {a, b} alphabete')
        print('  3: Binary adder machine')
        print('  4: Exit')
        option = 0
        while(not option in range(1, 5)):
            try:
                option = int(input("Insert option: "))
            except:
                print('Option should be a number between 1 and 4')
                continue
        
        if(option == 1):
            tapeDecimalSuccessor = [BLANK, BLANK, 9, 9, 9, BLANK, BLANK]
            testDecimalSuccessorMachine(tapeDecimalSuccessor, 2)
        elif(option == 2):
            tapePalindrome = [BLANK, BLANK, 'a', 'a', 'b', BLANK, BLANK]
            testPalindromeMachine(tapePalindrome, 2)
        elif(option == 3):
            tapeBinaryAdder = [BLANK, BLANK, 1, '+', 1, BLANK, BLANK]
            testBinaryAdderMachine(tapeBinaryAdder, 2)
        else:
            exit(0)
