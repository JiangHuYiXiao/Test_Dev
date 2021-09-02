# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/7/10 7:25
# @Software       : PyCharm
# @Python_verison : 3.7


from selenium import webdriver
from selenium.webdriver import Remote

# 启动浏览器驱动
def browser():
    '''
    定义浏览器函数，browser(),该函数可以进行配置，根据我们的需求可以配置测试用例在不同的主机及浏览器下运行，
    :return: driver
    '''
    # driver = webdriver.Chrome()
    host = '127.0.0.1:4444'     # 定义运行主机和端口号本机默认127.0.0.1，端口号默认4444
    dc = {'browser_name':'chrome'}      # 指定浏览器
    driver = Remote(command_executor='http://'+host+'/wd/hub',desired_capabilities=dc)
    return driver


if __name__=='__main__':
    dr = browser()
    dr.get('http://www.baidu.com')
    dr.quit()
