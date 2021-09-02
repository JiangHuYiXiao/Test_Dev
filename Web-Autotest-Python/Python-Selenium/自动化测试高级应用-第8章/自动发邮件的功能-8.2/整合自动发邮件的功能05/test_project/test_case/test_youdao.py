# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/5/16 7:30
# @Software       : PyCharm
# @Python_verison : 3.7
from selenium import webdriver
from unittest import TestCase
import unittest
import time
class Test_youdao(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_url = 'http://www.youdao.com'
        self.driver.get(self.base_url+'/')
        self.driver.implicitly_wait(20)
        print('test youdao start')
    def test_youdao(self):
        self.driver.find_element_by_css_selector('#translateContent').clear()
        self.driver.find_element_by_css_selector('#translateContent').send_keys('unittest')
        self.driver.find_element_by_css_selector('#form>button').click()
        time.sleep(5)
    def tearDown(self):
        self.driver.quit()
        print('test youdao end')

if __name__ == '__main__':
    unittest.main()

