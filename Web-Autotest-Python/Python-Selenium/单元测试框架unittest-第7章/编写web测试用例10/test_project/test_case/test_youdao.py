# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/4/28 8:48
# @Software       : Python-Selenium
# @Python_verison : 3.7
import unittest
import time
from selenium import webdriver
class Test_youdao(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = 'http://www.youdao.com'
        print('test youdao start')
    def test_youdao(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_css_selector('#translateContent').clear()
        driver.find_element_by_css_selector('#translateContent').send_keys('webdriver')
        driver.find_element_by_css_selector('#form > button').click()
        time.sleep(6)
        title = self.driver.title
        self.assertEqual(title,'【webdriver】什么意思_英语webdriver的翻译_音标_读音_用法_例句_在线翻译_有道词典',msg='title is not equal')

    def tearDown(self):
        self.driver.quit()
        print('test youdao end')

if __name__ == '__main__':
    unittest.main()




