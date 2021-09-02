# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/5/16 7:24
# @Software       : PyCharm
# @Python_verison : 3.7
# 解决了发送邮件、已经带附件的邮件还有怎么查找最新的测试报告这些问题，
# 我们就可以把自动发邮件的功能结合到我们自动化项目中。
import unittest
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from HTMLTestRunner import HTMLTestRunner
# from email.mime.multipart import MIMEMultipart

# 定义一个发送邮件的函数
def send_mail(file):
    f = open(file,'rb')
    mail_body = f.read()
    f.close()

    smtpservice = 'smtp.163.com'
    send_user = '18270717374@163.com'
    send_password = 'jianghu0313'
    sender = '18270717374@163.com'
    receiver = ['1721906562@qq.com','18270717374@163.com']
    # 邮件正文
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg['From'] = 'jianghu<18270717374@163.com>'
    msg['To'] = '1721906562@qq.com'

# 创建smtp实例
    smtp = smtplib.SMTP()
    smtp.connect(smtpservice)
    smtp.login(send_user,send_password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print('email has send out')

# 定义发送最新测试报告的函数
def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda x:os.path.getmtime(test_report + '\\' + x))
    report = os.path.join(test_report,lists[-1])
    print(report)
    return report

if __name__ == '__main__':
    report_dir = 'F:\\Python-Selenium\\自动化测试高级应用-第8章\\自动发邮件的功能-8.2\\整合自动发邮件的功能05\\test_project\\report'
    test_dir = 'F:\\Python-Selenium\\自动化测试高级应用-第8章\\自动发邮件的功能-8.2\\整合自动发邮件的功能05\\test_project\\test_case'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    now_time =time.strftime('%Y-%m-%d_%H_%M_%S')
    file_name = report_dir + '\\' + now_time + 'result.html'
    with open(file_name,'wb')as file:
        runner = HTMLTestRunner(stream=file,title='百度&有道测试报告',description='用例执行情况')
        runner.run(discover)
    # 调用发送最新报告的函数
    result = new_report(report_dir)
    # 发送邮件
    send_mail(result)
