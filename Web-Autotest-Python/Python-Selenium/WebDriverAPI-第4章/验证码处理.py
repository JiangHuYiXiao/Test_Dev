# -*- coding:utf-8 -*-
# 方法1：去掉验证码
# 直接注释掉验证码的那段代码

# 方法2：万能码

from random import randint
# randint用于生成一个范围内的随机整数
number = randint(1000,9999)
print(type(number),number)

# 输入随机数
input_number = input('请输入1000~9999范围内的随机数:')

# 判断
if number == int(input_number):
    print('登录成功')
elif int(input_number) == 1258:
    print('登录成功')
else:
    print('输入的验证码有误，登录失败')
# 方法3:：验证码识别技术

# 可以通过Python-tesseract来识别图片验证码

# 方法4：记录cookie
# 通过向浏览器中添加cookie可以绕过登陆的验证码，这是一个比较有意思的一种解决方法。

from selenium import webdriver
driver = webdriver.Chrome()
# 首次访问网站
driver.get('http://www.baidu.com')
# 获取所有的cookie信息
driver.get_cookies()
driver.add_cookie({'name':'user_name','value':'jianghu'})
driver.add_cookie({'name':'password','value':'1258'})
# 再次访问网站
driver.get('http://www.baidu.com')

driver.quit()
