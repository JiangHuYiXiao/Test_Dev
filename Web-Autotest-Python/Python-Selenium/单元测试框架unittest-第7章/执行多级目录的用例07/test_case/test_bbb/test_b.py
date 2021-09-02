#-*- coding:utf-8 -*-
import unittest

class Test_b(unittest.TestCase):
    def setUp(self):
        print('test b start')

    def test_c(self):
        print('test_b')

    def tearDown(self):
        print('test b end')


if __name__ == '__main__':
    unittest.main()