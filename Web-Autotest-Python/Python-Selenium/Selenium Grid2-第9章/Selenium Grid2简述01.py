# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/5/23 19:48
# @Software       : Python-Selenium
# @Python_verison : 3.7
# 在Selenium家族中我们已经学习了selenium webdriver，selenium ide， 本章我们将学习，selenium grid。
# selenium grid可以在不同的主机上建立主节点（hub）和分支节点（node），可以使主节点上的测试用例在不同的分支节点上运行，对不同的节点来说，可以搭建不同的测试环境（操作系统，浏览器），
# 从而使一份测试用例得到不同的环境下的测试结果。

# selenium grid版本和selenium是不对应的，grid2要晚于selenium的，但是grid2支持selenium2的所有功能。
# grid1和grid2的原理和基本工作方式是一致的，只是grid2同时支持selenium1和selenium2两种协议，并且在一些功能上做了优化，比如指定测试平台。
# selenium grid2不再提供单独的安装包，而是集成到selenium server中，所以，需要下载和运行selenium server才可以使用grid2的功能。