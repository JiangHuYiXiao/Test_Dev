# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/4/28 8:49
# @Software       : Python-Selenium
# @Python_verison : 3.7
import unittest
import time
import os
from HTMLTestRunner import HTMLTestRunner
test_dir ='E:\\Python-Selenium\\自动化测试高级应用-第8章\\HTML 测试报告-8.1\\项目集成测试报告06\\test_project\\test_case'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
if __name__ == '__main__':
    test_report_dir = 'E:\\Python-Selenium\\自动化测试高级应用-第8章\\HTML 测试报告-8.1\\项目集成测试报告06\\test_project\\report'
    now_time = time.strftime('%Y-%m-%d %H_%M_%S')
    # 生成到指定目录
    file_name = test_report_dir + '\\' + now_time + 'result.html'
    # 生成到当前目录
    # file_name = './' + now_time + 'result_html'
    with open(file=file_name,mode='wb') as file:
        runner = HTMLTestRunner(stream=file,title='测试报告',description='用例执行情况：')
        runner.run(discover)



# 生成测试报告需要到dos命令下执行
# F:\Python-Selenium\单元测试框架unittest-第7章\编写web测试用例10\test_project\python runtest.py >>report/log.txt 2>&1

