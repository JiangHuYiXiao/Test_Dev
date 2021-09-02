# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/5/14 8:32
# @Software       : Python-Selenium
# @Python_verison : 3.7
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
# 发送邮箱的服务器
server = 'smtp.163.com'
# 发送人
sender = '18270717374@163.com'
# 登录邮箱的用户名和密码
send_user = '18270717374@163.com'
send_password = 'jianghu0313'

# 接收邮箱的用户
receiver = '1721906562@qq.com'

# 创建一个带附件邮件的实例
message = MIMEMultipart()
# 往邮件容器中添加内容,这是邮件的主体
mail_title = '发送带附件的邮件'
mail_inside = MIMEText('这是我程序自动发送的,内含图片','plain','utf-8')
# 邮件的其他属性
message['Subject'] = Header(mail_title,'utf-8')
message['From'] = sender
message['To'] = receiver
message.attach(mail_inside)

# png附件
msgroot = MIMEText(open('F:\Python-Selenium\WebDriverAPI-第4章\\baidu_img.png','rb').read(),'base64','utf-8')
msgroot['Content_Type'] = 'application/octet-stream'
msgroot['Content_Disposition'] = 'attachment;filename="baidu_img.png"'
message.attach(msgroot)

# 连接发送邮件
smtp = smtplib.SMTP()           # 创建SMTP类的对象smtp
smtp.connect(server)
smtp.login(send_user,send_password)
smtp.sendmail(sender,receiver,message.as_string())
print('邮件发送成功')
smtp.quit()
