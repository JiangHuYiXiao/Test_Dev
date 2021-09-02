# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/4/12 9:00
# @Software       : Python-Selenium
# @Python_verison : 3.7

'''
需求：
    登录网易126邮箱
    用户名：jianghuyixiu   密码：jinaghu126
    用户名：yixiujianghu   密码：yixiu126
'''
from selenium import webdriver
import time
import login_126_mail
gdriver = webdriver.Chrome()
gdriver.maximize_window()
gdriver.implicitly_wait(10)
gdriver.get('https://mail.126.com/')
jianghu = login_126_mail.Login('jianghuyixiu','jinaghu126')
jianghu.login(gdriver)
gdriver.quit()
