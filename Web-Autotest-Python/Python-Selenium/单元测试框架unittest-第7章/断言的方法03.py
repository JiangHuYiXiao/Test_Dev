# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/4/18 18:51
# @Software       : Python-Selenium
# @Python_verison : 3.7
# 在执行用例的时候，判断用例是否通过，需要根据实际结果和预期结果进行对比。unittest框架下的TestCase类提供了下面的这些方法用于测试对比测试结果。
# 1、assertEqual(self, first, second, msg=None)      对比预期结果和实际结果是否相等,msg为可选参数，用于定义测试失败时打印的信息。
# 2、assertNotEqual(self, first, second, msg=None)   对比预期结果和实际结果是否不相等,msg为可选参数，用于定义测试失败时打印的信息。
# 3、assertTrue(self, expr, msg=None):               用于判断表达式expr是True吗,msg为可选参数，用于定义测试失败时打印的信息。
# 4、assertFalse(self, expr, msg=None):              用于判断表达式expr是False吗,msg为可选参数，用于定义测试失败时打印的信息。
# 5、assertIs(self, expr1, expr2, msg=None):         用于判断表达式expr1和expr2是否是同一个对象
# 6、assertIsNot(self, expr1, expr2, msg=None):      用于判断表达式expr1和expr2是否不是同一个对象
# 7、assertIsNone(self, obj, msg=None):              用于判断obj是是None
# 8、assertIsNotNone(self, obj, msg=None):           用于判断obj是不是None
# 9、assertIn(arg1, arg2, msg=None)	                 验证arg1是arg2的子串，不是则fail
# 10、assertNotIn(arg1, arg2, msg=None)	             验证arg1不是arg2的子串，是则fail
# 11、assertIsInstance(obj, cls, msg=None)	         验证obj是cls的实例，不是则fail
# 12、assertNotIsInstance(obj, cls, msg=None)	     验证obj不是cls的实例，是则fail
'''
from unittest import TestCase
import unittest
class Test_assert(TestCase):
    def setUp(self):
        a = input('请输入第一个数：')
        self.a = int(a)
        b = input('请输入第二个数：')
        self.b = int(b)
        print('test start')
    def test(self):
        self.assertEqual(self.a,self.b,msg='The Two Numbers Are Not Equal')
        # self.assertNotEqual(self.a,self.b,msg='The Two Numbers Is Equal')
        # self.assertTrue(self.a>self.b,msg='a<=b')
        # self.assertTrue(self.a<self.b,msg='a>=b')
        # self.assertIs(self.a,self.b)
        # self.assertIsNot(self.a,self.b)
        # self.assertIsNone(self.a,self.b)

    def tearDown(self):
        print('test end')
if __name__ == '__main__':
    unittest.main()
'''
from unittest import TestCase
from is_prime import Is_prime
import unittest
class Test_prime(TestCase):
    def setUp(self):
        print('test start')
    def test_prime(self):
        self.assertTrue(Is_prime(12).is_prime(),msg='Is not prime!')
    def tearDown(self):
        print('test end!')
if __name__ == '__main__':
    unittest.main()