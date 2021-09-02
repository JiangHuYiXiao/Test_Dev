# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/5/16 7:29
# @Software       : PyCharm
# @Python_verison : 3.7
from selenium import webdriver
import unittest
from unittest import TestCase
import time
class Test_baidu(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get('https://www.baidu.com')
        print('test baidu start')
    def test_baidu(self):
        self.driver.find_element_by_css_selector('#kw').clear()
        self.driver.find_element_by_css_selector('#kw').send_keys('webdriver')
        self.driver.find_element_by_css_selector('#su').click()
        time.sleep(5)
    def tearDown(self):
        self.driver.quit()
        print('test baidu end')

if __name__ == '__main__':
    unittest.main()