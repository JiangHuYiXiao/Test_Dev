
# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/4/28 8:49
# @Software       : Python-Selenium
# @Python_verison : 3.7
import unittest

test_dir ='F:\\Python-Selenium\\单元测试框架unittest-第7章\\编写web测试用例10\\test_project\\test_case'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
if __name__ == '__main__':
    unittest.TextTestRunner().run(discover)


# 生成测试报告需要到dos命令下执行
# F:\Python-Selenium\单元测试框架unittest-第7章\编写web测试用例10\test_project\python runtest.py >>report/log.txt 2>&1