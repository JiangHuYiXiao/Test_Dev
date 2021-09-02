# -*- coding:utf-8 -*-
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')
cookie = driver.get_cookies()
print(cookie)

# 添加cookie
driver.add_cookie({'name': 'jianghu','value':'yixiao'})
cook = driver.get_cookies()
for i in cook:
    print(i)
driver.quit()

'''
有时候我们需要验证浏览器中cookie是否正确，因为基于真实cookie的测试是无法通过白盒和集成测试进行的。WebDriver提供了操作Cookie的相关方法，可以读取、添加和删除cookie信息。

WebDriver操作cookie的方法：

get_cookies()： 获得所有cookie信息。

get_cookie(name)： 返回字典的key为“name”的cookie信息。

add_cookie(cookie_dict) ： 添加cookie。“cookie_dict”指字典对象，必须有name 和value 值。

delete_cookie(name,optionsString)：删除cookie信息。“name”是要删除的cookie的名称，“optionsString”是该cookie的选项，目前支持的选项包括“路径”，“域”。

delete_all_cookies()： 删除所有cookie信息。
'''