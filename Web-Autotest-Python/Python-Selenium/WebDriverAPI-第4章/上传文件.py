#-*- coding:utf-8 -*-
# 1、普通上传：适用于输入的标签为input标签
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://mail.163.com/')
iframe_id = driver.find_element_by_css_selector('div#loginDiv>iframe')
driver.switch_to.frame(iframe_id)
# 账号
driver.find_element_by_css_selector('div.u-input.box>input[data-loginname="loginEmail"]').clear()
driver.find_element_by_css_selector('div.u-input.box>input[data-loginname="loginEmail"]').send_keys('18270717374')
# 密码
driver.find_element_by_css_selector('.j-inputtext.dlpwd').clear()
driver.find_element_by_css_selector('.j-inputtext.dlpwd').send_keys('jiangtao0313')

# 登录
driver.find_element_by_css_selector('#dologin').click()
time.sleep(2)

# 警告框接受
# driver.switch_to.alert.dismiss()

# 写信
driver.find_element_by_css_selector('#_mail_component_24_24').click()
time.sleep(2)
# 上传文件
driver.find_element_by_css_selector('div>input.O0[type="file"][size="1"]').send_keys('F:\InstallConfig.ini')
time.sleep(10)
driver.quit()
'''

# 2、AutoIt实现上传
# AutoIt目前最新版是v3，他是一个使用类似BASIC脚本语言的免费软件。
# AutoIt用于Windows GUI的自动化测试，它利用模拟键盘按键，鼠标移动和窗口控件的组合来实现自动化任务。

# 第一步：
    # 打开AutoIt Windows Info工具，用鼠标单击Finder Tool，
    # 鼠标变成需要一个小风扇形状的图标，按住鼠标左键，将其拖动到识别的控件上步
# 选择文件：
    # Basic Windows Info： Title:打开  ，Class：#32770
    # Basic Control Info： Class：Edit ，Instance：1  所以classNN为Edit1
# 打开：
    # Basic Windows Info： Title:打开  ，Class：#32770   所以classNN为Button1
    # Basic Control Info： Class：Button ，Instance：1

# 第二步：
#打开SciTE Script Editor编辑器，编写AutoIt脚本

# 第三步：
# 将我们编写的upfile.au3生成为exe程序，打开Compile Script to.exe工具

# 第四步：
from selenium import webdriver
import os
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# 打开上传功能页面
file_path = os.path.abspath('upload.html')
driver.get(file_path)

# 点击上传功能按钮
driver.find_element_by_css_selector('input[type="file"]').click()
time.sleep(3)

os.system('F:\Python-Selenium\WebDriverAPI\\upfile.exe')
time.sleep(5)
driver.quit()