import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(5,3),8)
        self.assertEqual(add(10,4),14)
        self.assertEqual(add(5,5),10)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(10,8),2)
        self.assertEqual(sub(4,2),2)
        self.assertEqual(sub(6,3),3)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5,3), 15)
        self.assertEqual(mul(5, 1), 5)
        self.assertEqual(mul(5, 0), 0)

    #def test_divide(self): # 3 assertions
        #self.assertEqual(div(6, 3), 2)
        #self.assertEqual(div(10, 1), 10)
        #self.assertEqual(div(20,4), 5)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(log(2,8),3)
        self.assertAlmostEqual(log(10,10),10)
        self.assertAlmostEqual(log(5,1),0.0)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            log(0, 10)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            self.log(0, 10)
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self):# 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(5,12), 13)
        self.assertEqual(hypotenuse(7,24), 25)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(25),5)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(1), 1)
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            self.square_root(-4)
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()