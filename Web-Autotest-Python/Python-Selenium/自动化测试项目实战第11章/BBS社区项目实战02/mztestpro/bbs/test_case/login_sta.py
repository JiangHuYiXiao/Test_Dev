# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/7/10 7:22
# @Software       : PyCharm
# @Python_verison : 3.7
from time import sleep
import unittest,random,sys
sys.path.append('./models')
sys.path.append('./page_obj')
from models import myunit,function
from page_obj.login_page import Login_page

class Login_Test(myunit.Mytest):
    '''
    社区登录测试
    '''
    # 测试用户登录
    def user_login_verify(self,username='',password=''):
        Login_page(self.driver).user_login(username,password)

    def test_login1(self):
        '''用户名、密码为空登录'''
        self.user_login_verify()
        po = Login_page(self.driver)
        self.assertEqual(po.user_error_hint(),'请填写完整的登录信息')
        function.insert_img(self.driver,'user_pawd_empty.jpg')

    def test_login2(self):
        '''用户名正确、密码为空登录'''
        self.user_login_verify(username = '18270717374')
        po = Login_page(self.driver)
        self.assertEqual(po.user_error_hint(),'请填写完整的登录信息')
        function.insert_img(self.driver,'pawd_empty.jpg')

    def test_login3(self):
        '''用户名为空、密码正确登录'''
        self.user_login_verify(password='jianghu14')
        po = Login_page(self.driver)
        self.assertEqual(po.user_error_hint(), '请填写完整的登录信息')
        function.insert_img(self.driver, 'user_empty.jpg')

    def test_login4(self):
        '''用户名与密码不匹配'''
        character = random.choice('abcdefghijklmopkrstuvwxyz')
        username = '18270717374'+ character
        self.user_login_verify(username = username,password='jianghu14')
        po = Login_page(self.driver)
        self.assertEqual(po.user_error_hint(), '账号或密码错误')
        function.insert_img(self.driver, 'user_pawd_error.jpg')

    def test_login5(self):
        '''用户名与密码匹配'''
        self.user_login_verify(username='1820717374',password='jianghu14')
        po = Login_page(self.driver)
        self.assertEqual(po.user_login_success(), '社区')
        function.insert_img(self.driver, 'user_pawd_true.jpg')
if __name__ == '__main__':
    unittest.main()