#-*- coding:utf-8 -*-
# 1、Test Case：测试用例，包含setUp，run，tearDown
# 2、Test Suite：测试套件，多个测试用例组成一个测试套件,通过addTest加载TestCase到TestSuite中
# 3、Test Runner：通过unittest框架提供的TextTestRunner类提供的run()方法来执行测试用例或者套件。
# 4、Test Fixture：测试环境搭建和销毁，比如说setUp中建立数据库连接，在tearDown中清除数据库产生的数据，然后关闭连接。
from unit_test import Calculator
import unittest
class Test_Calculator(unittest.TestCase):
    def setUp(self):
        print('test start')
    def test_add(self):
        C1 = Calculator(2,3)
        self.assertEqual(C1.add(),5)
    def test_add1(self):
        C1 = Calculator(2,13)
        self.assertEqual(C1.add(),15)
    def test_add2(self):
        C1 = Calculator(2,13)
        self.assertEqual(C1.add(),11)
    def tearDown(self):
        print('test end')
if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    # 加载测试用例
    suite.addTest(Test_Calculator('test_add'))
    suite.addTest(Test_Calculator('test_add1'))
    suite.addTest(Test_Calculator('test_add2'))


    # 执行测试套件
    unittest.TextTestRunner().run(suite)        # 这种运行方式更加灵活，main方法是执行所有的

