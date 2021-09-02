# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/5/8 19:19
# @Software       : Python-Selenium
# @Python_verison : 3.7
# 将测试报告以邮件的方式发送给测试人员
# SMTP :简单邮件传输协议
# python的smtplib模块提供了一种很方便的途径来发送邮件，他对SMTP协议进行了简单的封装，我们可以使用SMTP对象的sendmail方法发送邮件，
# 常用方法：
# 1、connect(host,port) 连接邮箱服务器
# 2、login(user,password) 登录
# 3、sendmail(from_addr,to_addrs,msg,..) 发送邮件
# 4、quit() 结束会话

'''
发邮件的两种方式：
    方式1：Web端（qq邮箱、网易邮箱等），在网页填写，账号、密码进行登录,发送邮件时再填写对方邮箱地址及邮件标题、正文，完成后点击发送
    方式2：APP端（foxmail，outlook） ，APP填写账号、密码、邮箱服务器进行登录,发送邮件时再填写对方邮箱地址及邮件标题、正文，完成后点击发送

'''
# 我们Python更像是第二种方式进行发送邮件，因为需要填写服务器地址
import smtplib
smtp = smtplib.SMTP()
