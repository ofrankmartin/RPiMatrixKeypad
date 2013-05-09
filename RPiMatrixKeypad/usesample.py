import time

import RPi.GPIO as GPIO

from matrixkeypad import MatrixKeypad


def keypadTest():
    GPIO.setmode(GPIO.BOARD)
    mk = MatrixKeypad(rows = [15, 8, 10, 11], 
                      columns = [13, 19, 7], 
                      digits = [[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9],
                                ['*', 0, '#']])
    
    isFinished = False
    
    while not isFinished:
        mk.onUpdate()
        if not mk.readLastKey:
            digit = mk.getLastDigit()
            print(digit)
            
            if digit == '#':
                isFinished = True
        time.sleep(0.017)


if __name__ == '__main__':
    keypadTest()
    GPIO.cleanup()