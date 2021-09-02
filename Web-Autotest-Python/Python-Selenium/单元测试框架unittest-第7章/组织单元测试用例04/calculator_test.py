#-*- coding:utf-8 -*-

import unittest
# from calculator import add
from calculator import Calculator
class Test_add(unittest.TestCase):
    def setUp(self):
        print('test add start')
    def test_add(self):
        res = Calculator(1,3)
        self.assertEqual(res.add(),4,msg='add is error')
    def test_add2(self):
        res2 = Calculator(22,412)
        self.assertEqual(res2.add(),434,msg='add is error')
    def tearDown(self):
        print('test add end')
class Test_sub(unittest.TestCase):
    def setUp(self):
        print('test sub start')
    def test_sub(self):
        sub_res = Calculator(34,4)
        self.assertEqual(sub_res.sub(),30,msg='sub is error')
    def test_sub2(self):
        sub_res2= Calculator(1233,233)
        self.assertEqual(sub_res2.sub(),1000,msg='sub is error')
    def tearDown(self):
        print('test sub end')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test_add('test_add'))
    suite.addTest(Test_add('test_add2'))
    suite.addTest(Test_sub('test_sub'))
    suite.addTest(Test_sub('test_sub2'))

    unittest.TextTestRunner().run(suite)

# 通过测试结果我们可以看到setUp()和tearDown()方法分别作用于每个测试用例的开始和结尾，所以我们可以把setUp和tearDown进行封装下
import unittest
from calculator import Calculator
class Up_Down(unittest.TestCase):
    def setUp(self):
        print('test case start')
    def tearDown(self):
        print('test case end')

class Test_add(Up_Down):
    def test_add(self):
        t1 = Calculator(2,3)
        self.assertEqual(t1.add(),5,msg='add is error')
    def test_add2(self):
        t2 = Calculator(322,435)
        self.assertEqual(t2.add(),757,msg='add is error')
class Test_sub(Up_Down):
    def test_sub(self):
        t3 = Calculator(55,15)
        self.assertEqual(t3.sub(),40,msg='sub is error')
    def test_sub2(self):
        t4 = Calculator(34324,324)
        self.assertEqual(t4.sub(),34000,msg='sub is error')

# 全部运行
if __name__ == '__main__':
    unittest.main()

# 迭代执行
# if __name__ == '__main__':
#     suite= unittest.TestSuite()
#     suite.addTest(Test_add('test_add'))
#     suite.addTest(Test_add('test_add2'))
#     suite.addTest(Test_add('test_sub'))
#     suite.addTest(Test_add('test_sub2'))
#
#     unittest.TextTestRunner().run(suite)
