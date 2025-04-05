import random, time

class RangeException(Exception):
    pass

class Sensor():
    def __init__(self,min,max):
        if min > max:
            raise RangeException()
        self.min = min
        self.max = max


    def read_data(self):
       return (time.time(),random.uniform(self.min,self.max))

    