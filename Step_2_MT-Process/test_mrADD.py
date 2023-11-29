import unittest
import pandas as pd
from pandas.testing import assert_frame_equal

from mrADD import MR_ADD, _ttd

class TestMR_ADD(unittest.TestCase):
    def test_td_list(self):
        # Test _ttd with a list
        result = _ttd([1, 2, 3], 2)
        self.assertEqual(result, [3, 4, 5])

    def test_td_int(self):
        # Test _ttd with an integer
        result = _ttd(5, 2)
        self.assertEqual(result, 7)

    def test_followUP(self):
        # Test the followUP method
        mr_add = MR_ADD(6, 6, [1, 3], [4], 1, 2, 3, [])
        result = mr_add.followUP(2)
        expectedKeys = ['td_1', 'td_2', 'td_3', 'td_4', 'td_5', 'td_6', 'td_7', 'td_8', 
                        'ttd_1', 'ttd_2', 'ttd_3', 'ttd_4', 'ttd_5', 'ttd_6', 'ttd_7', 'ttd_8']
        keys = list(result.keys())
        
        self.assertEqual(expectedKeys, keys)
    
    def test_followUP2(self):
        # Test the followUP method
        mr_add = MR_ADD(6, 6, [1, 3], [4], 1, 2, 3, [])
        results = mr_add.followUP(2)

        # Create the expected DataFrame
        columns = ['td_1', 'td_2', 'td_3', 'td_4', 'td_5', 'td_6', 'td_7', 'td_8', 
                        'ttd_1', 'ttd_2', 'ttd_3', 'ttd_4', 'ttd_5', 'ttd_6', 'ttd_7', 'ttd_8']
        row = [6, 6, [1, 3], [4], 1, 2, 3, [],
               8, 8, [3, 5], [6], 3, 4, 5, []]
        
        expected = pd.DataFrame(columns=columns)
        expected.loc[0] = row
        
        # Compare the actual results with the expected DataFrame
        # print(results)
        # print('=====')
        # print(expected)
        assert_frame_equal(results, expected)

            

        # Add assertions here to check the DataFrame and other results

if __name__ == '__main__':
    unittest.main()