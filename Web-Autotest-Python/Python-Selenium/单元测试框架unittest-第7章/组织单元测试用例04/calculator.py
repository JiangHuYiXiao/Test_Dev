#-*- coding:utf-8 -*-
# 当我们增加被测功能和相应的用例后，再来看看unittest是如何扩展和组织新的测试用例的。

# 计算器类
class Calculator:
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
    # 加法
    def add(self):
        return self.a+self.b
    # 新增减法
    def sub(self):
        return self.a-self.b



