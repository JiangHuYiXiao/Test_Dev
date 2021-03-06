# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/5/2 8:56
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

# 硬断言（assert）
'''
1、assert （xx）xx         判断为真，一个布尔值，为true，用例执行成功，为false，用例执行失败
2、assert not （xx）
       ....        判断不为真，一个布尔值，为true，用例执行成功，不执行assert里面的语句，为false，用例执行失败，执行asset里面的语句
3、assert a in b           判断b包含a
4、assert a == b           判断a等于b
5、assert a != b           判断a不等于b

'''

'''
from time import sleep
from selenium import webdriver
import pytest
driver = webdriver.Chrome()

def test_baidu():
    driver.get('https://www.baidu.com/')
    sleep(2)
    assert (driver.title == '百度一下，你就知道')
def test_sohu():
    driver.get('http://www.sohu.com/')
    sleep(2)
    assert not (driver.title == '搜狐')
    print('用例执行失败')
    driver.quit()
'''

# 软断言（assume）
    # 断言失败后继续执行
    # 需要先安装pytest-assume插件：pip install pytest-assume
import pytest

class Test_DuanYan():
    def test_case1(self):
        pytest.assume(1==2)
        pytest.assume('i'=='hi')
        pytest.assume(2==2)
        print('test_case1')

    def test_case2(self):
        print('test_case2')

    def test_case3(self):
        print('test_case3')