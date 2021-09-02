# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/4/12 16:11
# @Software       : Python-Selenium
# @Python_verison : 3.7

from selenium import webdriver
import sys
# 添加路径
sys.path.insert(0,'F:\\Python-Selenium\\自动化测试模型-第5章')
import login_126_mail

jianghu = login_126_mail.Login('jianghuyixiu','jianghu126')
jianghu.login()
jianghu.logout()

yixiu = login_126_mail.Login('yixiujianghu','yixiu126')
yixiu.login()
yixiu.logout()
