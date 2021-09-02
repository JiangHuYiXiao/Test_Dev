# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/5/15 7:20
# @Software       : PyCharm
# @Python_verison : 3.7
# 现在已经知道如何通过Python自动发邮件，想要和自动化项目结合起来还需要解决一个问题，
# 但是我们报告的名称生成是按照时间来的，那么怎么找到最新的测试报告，这个是关键。
import os
result_dir = 'E:\\Python-Selenium\\自动化测试高级应用-第8章\\HTML 测试报告-8.1\\项目集成测试报告06\\test_project\\report'

# 列出该目录下的文件和子目录已经隐藏的文件,并且以列表的方式输出
lists = os.listdir(result_dir)

# 对列表进行排序sort,效率最高的排序
lists.sort(key=lambda x:os.path.getmtime(result_dir+'\\'+x))
print('最新的文件为：'+lists[-1])

# 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
file = os.path.join(result_dir,lists[-1])
print(file)


