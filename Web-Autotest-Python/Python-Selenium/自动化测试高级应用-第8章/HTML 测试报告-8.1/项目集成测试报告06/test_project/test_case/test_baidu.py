# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/4/28 8:48
# @Software       : Python-Selenium
# @Python_verison : 3.7
# 前面我们学习unittest的目的就是用它来运行web自动化测试用例，我们的目录机构如下。
'''
test_project/
|---test_case/
|   |---test_baidu.py
|   |---test_youdao.py
|---report/
    |---login_txt
|---runtest.py
'''
import unittest
from selenium import webdriver
import time
class Test_baidu(unittest.TestCase):
    '''百度测试类'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')

        print('test baidu start')
    def test_baidu(self):
        '''搜索关键字unittest框架'''
        self.driver.find_element_by_css_selector('#kw').clear()
        self.driver.find_element_by_css_selector('#kw').send_keys('unittest框架')
        self.driver.find_element_by_css_selector('#su').click()
        time.sleep(3)
        title = self.driver.title
        self.assertEqual(title,'unittest框架_百度搜索',msg='title is not equal')

    def tearDown(self):
        self.driver.quit()
        print('test baidu end')

if __name__ == '__main__':
    unittest.main()