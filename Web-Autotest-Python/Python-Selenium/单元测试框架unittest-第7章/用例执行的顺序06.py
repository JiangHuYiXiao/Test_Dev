#-*- coding:utf-8 -*-
# 用例执行顺序涉及多个层级，在多个测试目录下，先执行哪个目录，在多个测试文件下先执行哪一个文件，在多个测试类先执行哪个类？
# 我们这节主要学习用例执行的顺序问题
import unittest
class Bdd(unittest.TestCase):
    def setUp(self):
        print('test Bdd:')
    def test_ccc(self):
        print('test ccc')
    def test_aaa(self):
        print('test aaa')
    def tearDown(self):
        pass

class Add(unittest.TestCase):
    def setUp(self):
        print('test Add:')
    def test_bbb(self):
        print('test bbb')
    def tearDown(self):
        pass

# 根据ASCII码顺序执行
# if __name__ == '__main__':
#     unittest.main()

# 结果为：
# test Add:
# test bbb
# test Bdd:
# test aaa
# test Bdd:
# test ccc

# unittest框架默认根据ASCII码的顺序加载测试用例，数字和字母的顺序为：0-9，A-Z,a-z
# 所以Add会优先于Bdd，test_aaa优先于test_ccc
# 对于测试文件和测试目录也是如此，也可以按照指定的顺序执行，就是通过测试套件的方式，按照测试套件的加载顺序
if __name__ == '__main__':
    suite =unittest.TestSuite()
    suite.addTest(Bdd('test_ccc'))
    suite.addTest(Bdd('test_aaa'))
    suite.addTest(Add('test_bbb'))

    unittest.TextTestRunner().run(suite)