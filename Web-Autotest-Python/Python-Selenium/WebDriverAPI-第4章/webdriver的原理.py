#-*- coding:utf-8 -*-
# webdriver的原理就是我们常用的：serve-client模式
# 1、启动浏览器作为remote server
# 2、client（我们写的自动化代码）发送请求给remote server
# 3、remote server 依赖于浏览器驱动做出响应

# python提供了logging模块用于标准信息输出接口。提供了一个basicConfig()方法用于基本信息的定义，
# 开启debug模式就可以捕捉到client向remote server发送的请求
from selenium import webdriver
import logging
import time
logging.basicConfig(level=logging.DEBUG)
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
driver.find_element_by_css_selector('#kw').send_keys('selenium')
driver.find_element_by_css_selector('#su').click()
time.sleep(3)
driver.quit()

# 至于remote sever返回的信息，在后面学习selenium server时继续讲解