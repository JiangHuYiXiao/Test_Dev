# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/2/8 9:10
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from PageObject设计示例02.baidu import Baidu

def test_baidu():
    te = Baidu()
    print(te.click_map().get_text())

test_baidu()

