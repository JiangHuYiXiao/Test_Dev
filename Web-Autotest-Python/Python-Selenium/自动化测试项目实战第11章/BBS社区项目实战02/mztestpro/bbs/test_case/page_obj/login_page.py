# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/7/15 10:56
# @Software       : Python-Selenium
# @Python_verison : 3.7
from selenium.webdriver.common.action_chains import ActionChains            # 鼠标事件操作类
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class Login_page(Page):
    '''
    所有页面元素定位都在此层定义，UI一旦有更改，只需在修改这一层页面对象属性即可
    '''
    url = '/'
    # 点击登录图标后点击立即登录
    bbs_login_user_loc = (By.CSS_SELECTOR,'#bbs-avatar')
    bbs_login_button_loc = (By.CSS_SELECTOR,'#mzLogin')
    def bbs_login(self):
        self.find_element(*self.bbs_login_user_loc).click()
        sleep(1)
        self.find_element(*self.bbs_login_button_loc).click()

    login_username_loc = (By.CSS_SELECTOR,'#account')
    login_password_loc = (By.CSS_SELECTOR,'#password')
    # 验证码点击按钮
    login_click_loc = (By.CSS_SELECTOR,'#captcha2 > div > div.geetest_wait')
    # 登录按钮
    login_button_loc = (By.CSS_SELECTOR,'#login')
    # 登录用户
    def login_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)
    # 登录密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)
    # 登录验证码
    def login_click(self):
        self.find_element(*self.login_click_loc).click()
    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 定义统一登录入口
    def user_login(self,username='18270717374',password = 'jianghu14'):
        self.open()
        self.bbs_login()
        self.login_username(username)
        self.login_password(password)
        self.login_click()
        self.login_button()
        sleep(2)
    user_error_hint_loc = (By.CSS_SELECTOR,'#mainForm > div.tip-box > span.tip-font')
    user_login_success_loc = (By.CSS_SELECTOR,'#nv > div.bbs-logo > a > span')
    # 用户名或者密码不正确
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text
    # 登录成功用户名
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text

