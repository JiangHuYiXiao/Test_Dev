# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/5/20 8:29
# @Software       : Python-Selenium
# @Python_verison : 3.7
# Page Object设计模式是自动化测试项目开发实践的最佳设计模式之一，它主要体现在对界面交互细节的封装，这样就可以使测试案例更加关注与业务而非界面细节，从而提高了测试案例的可读性。

# Page Object设计模式的优点如下：
# 1、减少代码的重复
# 2、提高测试用力的可读性
# 3、提高测试用例的可维护性，尤其是针对UI频繁变化的项目

# 在我们实际软件开发中，页面的UI是可能改变的，如果每个测试用例中都有这个页面的UI元素被修改了，那么就是要去修改每个测试用例
# 如果我们把每个页面封装成一个对象，那么我们只需要修改这个对象的UI定位方法就可以，其他调用的地方不需要修改。
# 一个页面可以建立一个page对象，但是一些页面上的重要元素也可以建立一个对象，具体情况具体分析。


# Page Object模式主要是将页面中常用的功能封装成一个对象，对外提供接口进行调用，当我们的页面元素组件发生改变时，我们的测试用例只需要修改封装的细节内容，
# 而不需要去修改调用的测试用例，这大大的减少了我们的代码重复性。在其他方面也是可以使用的，简单粗暴理解，一切都是对象，将常用的功能代码进行封装，对外提供接口方法调用。
# 我们的断言和page对象尽量分开在不同的文件中

# 下面以登录163邮箱为例
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import selenium

class Page:
    '''
    基础类，用于页面对象的继承初始化
    '''
    login_url = 'https://mail.163.com'
    def __init__(self,driver,base_url = login_url):
        self.driver = driver
        self.base_url = base_url
    # 对URL地址进行断言
    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    # 打开url
    def _open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(),'Did not land on %s' % url
    # 打开url，本身没有做任何事情，交给_open()方法实现
    def open(self):
        self._open(self.url)
    #  元素定位
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

class Login_page(Page):     # 继承Page类
    '''
    登录页面对象
    '''
    url = '/'
    # 定位
    def iframe(self,driver):
        iframe_id = driver.find_element_by_css_selector('div.loginUrs>iframe')
        # 切换到iframe
        driver.switch_to.frame(iframe_id)
    username_loc = (By.CSS_SELECTOR,'.j-inputtext.dlemail')
    password_loc = (By.CSS_SELECTOR,'.j-inputtext.dlpwd')
    submmit_loc = (By.CSS_SELECTOR,'#dologin')

    # Action
    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)
    def type_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)
    def type_submmit(self):
        self.find_element(*self.submmit_loc).click()

def test_user_login(driver,username,password):
    '''
    测试获取的用户名、密码是否可以登录
    '''

    lp = Login_page(driver)
    lp.open()
    lp.iframe(driver)
    lp.type_username(username)
    lp.type_password(password)
    lp.type_submmit()

def main():
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        username = '18270717374'
        password = 'jianghu0313'

        driver.implicitly_wait(20)
        test_user_login(driver,username,password)
        time.sleep(5)
        text = driver.find_element_by_css_selector('.js-component-component.gWel-greet-trueName>span').text
        assert (text =='jianghu'),'用户名称不匹配，登录失败'

    finally:
        driver.close()

if __name__ == '__main__':
    main()
