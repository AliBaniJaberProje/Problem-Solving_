import unittest
import SwapTwoNumberWithOutUseTMP as Swap

class MyTestCase(unittest.TestCase):
    def test_something(self):
        my_test_val = {"num1": 10, "num2": 20}
        my_test_result=Swap.swap_tow_number_with_out_use_tmp(my_test_val)
        self.assertEqual(my_test_val["num1"], my_test_result["num2"])
        self.assertEqual(my_test_val["num2"], my_test_result["num1"])



if __name__ == '__main__':
    unittest.main()
