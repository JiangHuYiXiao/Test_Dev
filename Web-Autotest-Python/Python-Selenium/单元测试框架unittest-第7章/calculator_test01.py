#-*- coding:utf-8 -*-
# 单元测试的方法
# 1、自己编写代码来进行单元测试，不通过单元测试框架
# from unit_test import Calculator
class Test_calculator:
    def test_add(self):
        try:
            a1 = Calculator(1,3)
            res = a1.add()
            assert(res == 43)
        except AssertionError:
            print('Integer addition result error')
        else:
            print('Test pass!')
t1 = Test_calculator()
t1.test_add()

# assert():
# if 条件为False：
#     程序引发AssertionError错误

# 2、通过单元测试框架编写测试单元测试代码
from unit_test import Calculator
import unittest
class Test_calculator(unittest.TestCase):
    def setUp(self):            # 开始 环境搭建
        print('test start')
    def test_add(self):         # 测试用例一定要以test开头
        C1 = Calculator(1,4)            # 实例化，创建对象
        self.assertEqual(C1.add(),5)            # 使用unittest框架提供的断言方法，判断两者是否相等
    def tearDown(self):
        print('test end')       # 结尾，环境还原

if __name__ == '__main__':
    unittest.main()         # 使用它可以将一个单元测试模块变成一个可执行的脚本，
                            # main()方法使用TestLoader类来搜索所有包含在该模块中以test命名的测试方法，并自动执行他们