# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/4/12 9:34
# @Software       : Python-Selenium
# @Python_verison : 3.7
from selenium import webdriver
import time
class Login:
    def __init__(self,user_name,password):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://mail.126.com')
        self.user_name = user_name
        self.password = password
    def login(self):
        iframe_id = self.driver.find_element_by_css_selector('div.loginUrs>iframe')
        self.driver.switch_to.frame(iframe_id)
        # 用户名
        self.driver.find_element_by_css_selector('.j-inputtext.dlemail.j-nameforslide').clear()
        self.driver.find_element_by_css_selector('.j-inputtext.dlemail.j-nameforslide').send_keys(self.user_name)
        # 密码
        self.driver.find_element_by_css_selector('.j-inputtext.dlpwd').clear()
        self.driver.find_element_by_css_selector('.j-inputtext.dlpwd').send_keys(self.password)
        # 登录
        self.driver.find_element_by_css_selector('#dologin').click()
        time.sleep(2)
        # 登录截图
        self.driver.get_screenshot_as_file('F:\Python-Selenium\自动化测试模型\%s_mail.126.png'%(self.user_name))
        # 验证登录是否成功
        login_answer = self.driver.find_element_by_css_selector(
            'div.gWel-top.gWel-top-hasAvatar>div.gWel-greet>span>span').text

        if login_answer == self.user_name:
            print('%s:登录成功' % (self.user_name))
        else:
            print('登录失败')
    def logout(self):
        self.driver.find_element_by_link_text('退出').click()
        print('%s:退出成功'%(self.user_name))
        self.driver.quit()