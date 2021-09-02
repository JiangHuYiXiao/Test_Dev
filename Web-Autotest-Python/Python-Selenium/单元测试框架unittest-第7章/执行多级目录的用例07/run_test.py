#-*- coding:utf-8 -*-
import unittest
# 定义测试用例的目录
test_dir = './test_case'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ == '__main__':
    unittest.TextTestRunner().run(discover)
# 当定义的测试目录为test_case时，只有test_a.py会执行测试，
# 怎么样让unittest框架找到test_case子目录中的测试文件呢？
# 方法为：在每个子目录下添加一个__init__.py文件，用来标识这是一个标准包含了Python模块的目录


