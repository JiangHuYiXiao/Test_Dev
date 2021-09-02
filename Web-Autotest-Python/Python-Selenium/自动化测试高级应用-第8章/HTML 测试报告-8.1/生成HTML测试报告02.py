# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/5/5 8:07
# @Software       : PyCharm
# @Python_verison : 3.7
# 下面继续以test_baidu.py为例生成HTMLTestRunner为测试报告
import unittest
import time
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
class Test_baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.base_url = 'http://www.baidu.com'
        print('test baidu start')
    def test_baidu(self):
        self.driver.get(self.base_url + '/')
        self.driver.find_element_by_css_selector('#kw').clear()
        self.driver.find_element_by_css_selector('#kw').send_keys('selenium')
        self.driver.find_element_by_css_selector('#su').click()
        time.sleep(5)
    def tearDown(self):
        self.driver.quit()
        print('test baidu end')

# 普通运行在命令窗口输出
'''
if __name__ == '__main__':
    # 定义测试套件
    suite = unittest.TestSuite()
    # 套件中添加用例
    suite.addTest(Test_baidu('test_baidu'))
    # 定义测试用例的目录
    test_dir = './'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    unittest.TextTestRunner().run(discover)
'''
print(__name__)
if __name__ == '__main__':
    # 定义测试套件
    suite = unittest.TestSuite()
    # 套件中添加用例
    suite.addTest(Test_baidu('test_baidu'))
    # 定义报告
    file = open('./result.html','wb')
    runner = HTMLTestRunner(stream=file,title='百度搜索测试报告',description='用例执行情况:')
    # 运行测试用例
    runner.run(suite)
    # 关闭报告
    file.close()
