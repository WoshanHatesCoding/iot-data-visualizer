
from device import*
from dashboard import *
from tests import *

import unittest

if __name__ == '__main__':
    unittest.main(exit=False)
    dashboard = Dashboard()
    cm = Communication(on_send=dashboard.display_analytics)
    d = Device(communication=cm)
    while True:
        for i in range(10):
            d.get_data()
        d.process_data()
        plt.pause(0.01)

    

    