# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/4/19 8:45
# @Software       : Python-Selenium
# @Python_verison : 3.7
# 判断一个数是否是质数
class Is_prime:
    def __init__(self,number):
        self.number = number
    def is_prime(self):
        if self.number <= 1:
            return False
        else:
            for i in range(2,self.number):
                if self.number % i ==0:
                    return False
                else:
                    return True

if __name__ == '__main__':
    i1 = Is_prime(100)
    print(i1.is_prime())
