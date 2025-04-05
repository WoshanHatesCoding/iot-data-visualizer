import random, statistics

class DataProcessor: 
    def max(self,sequence):
        return max([i[1] for i in sequence])

    def min(self,sequence):
        return min([i[1] for i in sequence])

    def average(self,sequence):
        return statistics.mean([i[1] for i in sequence])
