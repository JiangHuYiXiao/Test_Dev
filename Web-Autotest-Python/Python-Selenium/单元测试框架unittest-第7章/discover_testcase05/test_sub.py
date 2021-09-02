# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/4/22 19:48
# @Software       : Python-Selenium
# @Python_verison : 3.7
import unittest
from calculator import Calculator
class Test_sub(unittest.TestCase):
    def setUp(self):
        print('test case start')
    def test_sub(self):
        c3 = Calculator(54,34)
        self.assertEqual(c3.sub(),20,msg='sub is error')
    def test_sub2(self):
        c4 = Calculator(4444223,223)
        self.assertEqual(c4.sub(),4444000,msg='sub is error')
    def tearDown(self):
        print('test case end')

if __name__ == '__main__':
    unittest.main()

#程序不被调用这种套件的方式运行更加合理，但是一般都会被调用，运行测试用例有专门的运行文件，所以不建议用这个方式运行
# 构建测试套件
'''
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test_sub('test_sub'))
    suite.addTest(Test_sub('test_sub2'))
    
# 运行
    unittest.TextTestRunner().run(suite)
    '''