# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/7/10 7:26
# @Software       : PyCharm
# @Python_verison : 3.7
from selenium import webdriver
from .driver import browser
import unittest
import os
'''
自定义测试框架类，Mytest用于继承unittest.TestCase类，因为如果你在所有创建的测试用例中setUp()和tearDown()方法所做的事一样，所以把他们抽象成MyTest类
好处是在编写测试用例时候不用考虑着两个方法的实现。
'''
class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
