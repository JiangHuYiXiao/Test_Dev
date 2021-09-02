# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/4/22 19:48
# @Software       : Python-Selenium
# @Python_verison : 3.7

import unittest
from test_add import Test_add
from test_sub import Test_sub
suite = unittest.TestSuite()
suite.addTest(Test_add('test_add'))
suite.addTest(Test_add('test_add2'))
suite.addTest(Test_sub('test_sub'))
suite.addTest(Test_sub('test_sub2'))

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)

# 这样设计看上去更加完美，但是依然没有解决添加用例的问题，如果我们有很多用例需要添加，如果一直在run_test.py下面添加
# 也是相当麻烦的，unittest中提供了一个TestLoader类的discover()方法可以解决这个问题。

# TestLoader类
# 负责根据各种标准加载测试用例，并将它们返回给测试套件，正常情况下不需要创建这个类的实例。
# unittest提供了可以共享的defaultTestLoader类，可以使用其子类和方法创建实例，discover()就是其中之一。
# unittest.TestLoader.discover()
# def discover(self, start_dir, pattern='test*.py', top_level_dir=None)
# start_dir 要测试的模块名或者测试用例的目录
# pattern='test*.py' 表示用例文件名的匹配原则
# top_level_dir=None 表示测试模块的顶层目录
'''
import unittest
# 定义测试用例的目录为当前目录
# test_dir= './'
test_dir= 'F:\Python-Selenium\单元测试框架unittest\discover_testcase05'    #
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ == '__main__':
    unittest.TextTestRunner().run(discover)
'''