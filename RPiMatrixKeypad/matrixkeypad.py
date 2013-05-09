import RPi.GPIO as GPIO
from timer import Timer

class MatrixKeypad:
    """Class used to read the key interruptions from a matrix keypad"""

    def __init__(self, rows, columns, digits = [], keyRepeatInterval = 300):
        """Initializes the keypad

        Keyword arguments:
        rows -- a list containing the rows input GPIO pin
        columns -- a list containing the columns output GPIO pin
        digits -- a bi-dimensional list with the keypad symbols
        keyRepeatInterval -- key repeat interval in milliseconds
        """
        self.rows = rows
        self.columns = columns
        self.digits = digits
        self.keyTimer = Timer(keyRepeatInterval)
        self.keyTimer.finished = True
        self.readLastKey = True
        
        for r in self.rows:
            GPIO.setup(r, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
        for c in self.columns:
            GPIO.setup(c, GPIO.OUT)

        self.lastKey = (None, None)


    def onUpdate(self):
        self.keyTimer.onUpdate()
        for j, c in enumerate(self.columns):
            GPIO.output(c, True)

            for i, r in enumerate(self.rows):
                if GPIO.input(r):
                    if self.keyTimer.isFinished() or self.lastKey != (i, j):
                        self.keyTimer.start()
                        self.lastKey = (i, j)
                        row, col = self.lastKey
                        self.readLastKey = False
                    
            GPIO.output(c, False)


    def getLastKey(self):
        """Get the last key position

        Return:
        A tuple with (row, column) value
        """
        self.readLastKey = True
        return self.lastKey


    def getLastDigit(self):
        """Get the last digit typed

        Return:
        A digit from the list of digits if this list is populated.
        Otherwise returns None
        """
        r, c = self.getLastKey()
        if len(self.digits) > 0 and not (r == None or c == None):
            return self.digits[r][c]
        else:
            return None
