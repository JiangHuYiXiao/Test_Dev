#-*- coding:utf-8 -*-
import unittest

class Test_a(unittest.TestCase):
    def setUp(self):
        print('test a start')

    def test_c(self):
        print('test_a')

    def tearDown(self):
        print('test a end')


if __name__ == '__main__':
    unittest.main()