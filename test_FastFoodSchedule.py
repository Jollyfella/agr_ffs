
#standard python stuff
import unittest
import pandas as pd

#custom python stuff
import FastFoodSchedule



# check fot expected output

class Test_Schedule(unittest.TestCase):
        
    def setUp(self):
        # capture results of funtion
        self.orders = 3
        

    def tearDown(self):
        pass
                      
    def test_orders(self):
        result = FastFoodSchedule.orders(self.orders)
        #Number of orders placed should be int
        self.assertIsInstance(self.orders, int, msg='orders should be an int dtype')
        #Number of orders placed should be greater then 0
        self.assertNotEqual(self.orders, 0, msg='number of orders placed should be greater than zero')
        #Result should return dataframe object
        self.assertIsInstance(result,object, msg='Result should return dataframe object')
        #Timestamp format in dataframe should be type string
        self.assertIsInstance(result['time'][1],str, msg='Timestamp in dataframe should be type string')
        #Timestamp should have format '{:%H:%M:%S}'
        self.assertRegex(result['time'][1],'\d{2}\:\d{2}\:\d{2}', msg="Timestamp should have format {:%H:%M:%S}")
        
    def test_output_schedule_type(self):
        # print output should be a dataframe object
        result2 = FastFoodSchedule.output_schedule(FastFoodSchedule.orders(self.orders))
        self.assertIsInstance(result2,object, msg='print output should be a dataframe object')
        
if __name__ == '__main__':
    unittest.main()