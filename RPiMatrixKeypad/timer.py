import time


class Timer:
    def __init__(self, millis, isLoop = False):
        self.millis = millis
        self.isLoop = isLoop
        self.startTime = int(round(time.time() * 1000))
        self.running = False
        self.finished = False
        self.start()
        pass
    
    
    def start(self):
        self.startTime = int(round(time.time() * 1000))
        self.running = True
        self.finished = False
    
    
    def onUpdate(self):
        currTime = int(round(time.time() * 1000))
        if self.running and currTime - self.startTime >= self.millis:
            self.finished = True
    
            if self.isLoop:
                self.startTime = currTime
            else:
                self.running = False


    def isFinished(self):
        ret = self.finished
        if self.isLoop and self.finished:
            self.finished = False

        return ret


    def stop(self):
        self.running = False

    
    def setTime(self, millis):
        self.millis = millis