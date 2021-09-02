# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/7/10 7:23
# @Software       : PyCharm
# @Python_verison : 3.7
'''
编写Page Object，关于page object设计模式，之前我们已经学习过，这里我们将使用该设计模式进行编写测试用例
首先创建page基础类

'''
class Page:
    '''
    页面基础类，用于所有页面的继承
    '''
    login_url = 'https://bbs.meizu.cn'
    def __int__(self,driver,base_url = login_url,parent = None):
        self.base_url = base_url
        self.driver = driver
        self.parent = parent
        self.timeout = 30

    # 为了对url地址进行断言
    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    # 打开url
    def _open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(),'Did not land on %s'%url
    # 重写元素定位方法
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    # 重写元素定位方法多个元素
    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)
    # 调用java script脚本
    def script(self,src):
        return self.driver.execute_script(src)


