# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/4/22 19:43
# @Software       : Python-Selenium
# @Python_verison : 3.7

class Calculator:
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
    def add(self):
        return (self.a + self.b)
    def sub(self):
        return (self.a - self.b)
