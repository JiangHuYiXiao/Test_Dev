# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/5/7 7:36
# @Software       : PyCharm
# @Python_verison : 3.7
# 现在的测试报告还不易读，因为他只列了一堆测试类Test_baidu和测试方法test_baidu，测试类和测试方法的命名可读性不好，
# 时间久了就不知道这个报告测试的是啥内容。在编写功能测试用例时每条用例都有标题，那么我们能不能给自动化用例也加上标题呢，在此之前我们学习过python的注释
# python的注释有两种，comment，另一种叫doc string，前者为普通注释，后者为函数和方法的描述。
'''
class Add:
    ''Add类包含add方法''
    def add(self,a,b):
        ''add方法需要两个参数a,b,并且返回两个参数相加的结果''
        return a + b

print(Add.__name__)
print(Add.__doc__)
print(Add.add.__doc__)
help(Add)
help(Add.add)
'''
import unittest
import time
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
class Test_baidu(unittest.TestCase):
    '''百度搜索测试'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.base_url = 'http://www.baidu.com'
        print('test baidu start')
    def test_baidu(self):
        '''搜索selenium关键字'''
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
    file = open('./result1.html','wb')
    runner = HTMLTestRunner(stream=file,title='百度搜索测试报告',description='用例执行情况:')
    # 运行测试用例
    runner.run(suite)
    # 关闭报告
    file.close()