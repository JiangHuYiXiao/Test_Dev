#-*- coding:utf-8 -*-
import unittest
class Test_c(unittest.TestCase):
    def setUp(self):
        print('test c start')
    def test_c(self):
        print('test_c')
    def tearDown(self):
        print('test c end')


if __name__ == '__main__':
    unittest.main()