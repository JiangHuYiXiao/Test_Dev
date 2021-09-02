#-*- coding:utf-8 -*-
# 1、单元测试框架的特点:
#     提供用例组织和执行
#     提供丰富的比较方法
#     提供丰富的日志
# 不用单元框架我们也可以进行单元测试，所谓的单元测试就是通过一段代码去验证另一段代码。

# 举个例子，不用单元框架进行单元测试：
# 计算器类
class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return (self.a + self.b)

    def reduce(self):
        return self.a - self.b