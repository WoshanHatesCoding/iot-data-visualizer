from sensor import *
from communication import *
from data_processor import *


class Device:
    def __init__(self, sensor = Sensor(1,100), data_processor=DataProcessor(), communication = Communication()):
        self.sensor = sensor
        self.data_processor = data_processor
        self.communication = communication
        self.data = []

    def get_data(self):
        self.data.append(self.sensor.read_data())
    
    def process_data(self):
        data={
            "min": self.data_processor.min(self.data),
            "max": self.data_processor.max(self.data),
            "avarage": self.data_processor.average(self.data),
            "time":self.data[-1][0]
        }
        self.data=[]
        self.communication.send_data(data)