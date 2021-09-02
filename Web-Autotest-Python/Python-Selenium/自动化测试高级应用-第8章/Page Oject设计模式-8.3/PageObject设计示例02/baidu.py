# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/2/8 8:56
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from PageObject设计示例02.map import Map
class Baidu():
    '''
    百度page页,包含了搜索方法、点击方法、标题方法
    '''
    def search(self):
        pass
    def click(self):
        pass
    def title(self):
        pass

    '''
    在百度首页点击地图链接跳转到百度地图页面
    需要在跳转之前的page页面对象中return跳转后的类，也就是返回跳转后的page页面的一个实例，这样我们可以直接调用跳转后的page页面的方法
    '''
    def click_map(self):
        # click
        return Map()