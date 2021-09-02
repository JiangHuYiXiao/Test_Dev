# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/4/24 19:02
# @Software       : Python-Selenium
# @Python_verison : 3.7

# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : ${DATE} ${TIME}
# @Software       : ${PROJECT_NAME}
# @Python_verison : 3.7
# 前面我们已经讲过fixture指的是setUp和tearDown，其次unittest提供了更大范围的fixtures，例如对于测试类和模块的fixtures
import unittest
def setUpModule():
    print('test module start >>>>>>')
def tearDownModule():
    print('test module end >>>>>>')


class Test(unittest.TestCase):
    @classmethod
    # 当这个方法的操作只涉及静态属性时，就应该用classmathod来装饰这个方法
    def setUpClass(cls):
        print('test class start >>>>>>')
    @classmethod
    def tearDownClass(cls):
        print('test class end >>>>>>')
    def setUp(self):
        print('test case start >>>>>>')
    def tearDown(self):
        print('test case end >>>>>>')
    def test_case(self):
        print('test_case -->')
    def test_case2(self):
        print('test case2 -->')

if __name__ == '__main__':
    unittest.main()

# 结果为：
'''
test module start >>>>>>
test class start >>>>>>
test case start >>>>>>
test_case -->
test case end >>>>>>
test case start >>>>>>
test case2 -->
test case end >>>>>>
test class end >>>>>>
test module end >>>>>>
'''


