# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/5/10 8:42
# @Software       : Python-Selenium
# @Python_verison : 3.7
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送邮箱的服务器
smtpservice = 'smtp.163.com'
# 登录邮箱的用户名密码
send_user = '18270717374@163.com'
send_password = 'jianghu0313'
# 发送邮箱
sender = '18270717374@163.com'
# 接收邮箱
receiver = ['1721906562@qq.com','18270717374@163.com']
# 发送邮箱的主题
subject = 'python email send'

# 编写HTML类型的邮件正文
msg = MIMEText('<html><h1>你好！！欢迎使用html格式</h1></html>','html','utf-8')
msg['Subject'] = Header(subject,'utf-8')
msg['From'] = 'jianghu<18270717374@163.com>'
msg['To'] =  '1721906562@qq.com'


# 连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpservice)
smtp.login(send_user,send_password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()