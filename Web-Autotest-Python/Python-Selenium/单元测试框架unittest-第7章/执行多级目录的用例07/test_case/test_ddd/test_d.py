#-*- coding:utf-8 -*-
import unittest

class Test_d(unittest.TestCase):
    def setUp(self):
        print('test d start')

    def test_c(self):
        print('test_d')

    def tearDown(self):
        print('test d end')


if __name__ == '__main__':
    unittest.main()