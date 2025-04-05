from __main__ import *
import unittest
from unittest.mock import Mock, patch
from datetime import datetime


class TestCommunication(unittest.TestCase):
    def setUp(self):        
        self.communication = Communication(
            on_send=lambda data: None,
            on_receive=lambda: None
        )
    
    def test_send_data_with_callback(self):        
        def mock_send_callback(data):
            self.sent_data = data
        
        
        self.communication.on_send = mock_send_callback
        
        
        test_data = "Hello, world!"
        self.communication.send_data(test_data)
        
        
        self.assertEqual(self.sent_data, test_data)
    
    def test_receive_data_with_callback(self):
        
        def mock_receive_callback():
            self.received_data = True
        
        
        self.communication.on_receive = mock_receive_callback
        
        
        test_data = "Hello, world!"
        self.communication.receive_data(test_data)
        
        
        self.assertTrue(self.received_data)



class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = DataProcessor()
        self.sequence = [(1, 10), (2, 20), (3, 30)]

    def test_max(self):
        result = self.processor.max(self.sequence)
        self.assertEqual(result, 30)

    def test_min(self):
        result = self.processor.min(self.sequence)
        self.assertEqual(result, 10)

    def test_average(self):
        result = self.processor.average(self.sequence)
        self.assertEqual(result, 20)


class TestDevice(unittest.TestCase):
    def setUp(self):
        self.mock_sensor = Mock(spec=Sensor)
        self.mock_data_processor = Mock(spec=DataProcessor)
        self.mock_communication = Mock(spec=Communication)
        self.device = Device(sensor=self.mock_sensor,
                             data_processor=self.mock_data_processor,
                             communication=self.mock_communication)

    def test_get_data(self):
        
        self.mock_sensor.read_data.return_value = (datetime.now(), 42)

        
        self.device.get_data()

        
        self.assertEqual(self.device.data, [(datetime.now(), 42)])

    def test_process_data(self):
        
        self.device.data = [(datetime(2022, 1, 1, 0, 0, 0), 10),
                            (datetime(2022, 1, 1, 0, 0, 1), 20),
                            (datetime(2022, 1, 1, 0, 0, 2), 30)]

        
        expected_data = {
            "min": 10,
            "max": 30,
            "average": 20,
            "time": datetime(2022, 1, 1, 0, 0, 2)
        }

        
        self.mock_communication.send_data.return_value = None

        
        self.device.process_data()

        
        self.mock_data_processor.min.assert_called_once_with([(datetime(2022, 1, 1, 0, 0, 0), 10),
                                                              (datetime(2022, 1, 1, 0, 0, 1), 20),
                                                              (datetime(2022, 1, 1, 0, 0, 2), 30)])
        self.mock_data_processor.max.assert_called_once_with([(datetime(2022, 1, 1, 0, 0, 0), 10),
                                                              (datetime(2022, 1, 1, 0, 0, 1), 20),
                                                              (datetime(2022, 1, 1, 0, 0, 2), 30)])
        self.mock_data_processor.average.assert_called_once_with([(datetime(2022, 1, 1, 0, 0, 0), 10),
                                                                  (datetime(2022, 1, 1, 0, 0, 1), 20),
                                                                  (datetime(2022, 1, 1, 0, 0, 2), 30)])
        self.assertEqual(self.device.data, [])

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.sensor = Sensor(1, 100)

    def test_init_valid_range(self):
        self.assertEqual(self.sensor.min, 1)
        self.assertEqual(self.sensor.max, 100)

    def test_init_invalid_range(self):
        with self.assertRaises(RangeException):
            Sensor(100, 1)

    @patch('sensor.time.time', return_value=12345.6789)
    @patch('sensor.random.uniform', return_value=50)
    def test_read_data(self, mock_uniform, mock_time):
        data = self.sensor.read_data()
        self.assertEqual(data[0], 12345.6789)
        self.assertEqual(data[1], 50)