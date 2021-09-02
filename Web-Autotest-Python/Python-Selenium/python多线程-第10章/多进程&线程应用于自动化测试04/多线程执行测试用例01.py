# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/6/24 6:58
# @Software       : PyCharm
# @Python_verison : 3.7

# 百度首页测试

import unittest
from threading import Thread
from selenium import webdriver
from time import ctime,sleep

def test_baidu(browser,search):
    print('start %s:'% (ctime()))
    print('browser %s:'% browser)
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'ie':
        driver = webdriver.Ie()
    else:
        print('browser 参数有误，只能为ie，firefox，chrome')
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get('https://www.baidu.com/')
    # 搜索
    driver.find_element_by_css_selector('#kw').clear()
    driver.find_element_by_css_selector('#kw').send_keys(search)
    # 点击
    driver.find_element_by_css_selector('#su').click()
    sleep(5)
    driver.quit()
    print('test case end!')

if __name__ =='__main__':
    # 启动参数，指定浏览器驱动和搜索的内容
    dicts = {'ie':'selenium','chrome':'霸王别姬','firefox':'悟空'}
    # 创建线程
    threads = []
    for browser,search in dicts.items():
        t1 = Thread(target=test_baidu,args=(browser,search))
        threads.append(t1)
    # 启动线程
    for i in threads:
        i.start()
    for  i in threads:
        i.join()
    print('all end %s'%ctime())


# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.get('http://www.baidu.com')
