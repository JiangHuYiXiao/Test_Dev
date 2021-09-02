# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/4/22 19:48
# @Software       : Python-Selenium
# @Python_verison : 3.7
import unittest
from calculator import Calculator
class Test_add(unittest.TestCase):
    def setUp(self):
        print('test case start')
    def test_add(self):
        c1 = Calculator(21,12)
        self.assertEqual(c1.add(),33,msg='add is error')
    def test_add2(self):
        c2 = Calculator(2133,33)
        self.assertEqual(c2.add(),2166,msg='add is error')
    def tearDown(self):
        print('test case end')

if __name__ == '__main__':
    unittest.main()


'''
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test_add('test_add'))
    suite.addTest(Test_add('test_add2'))

    unittest.TextTestRunner().run(suite)
'''