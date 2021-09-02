#-*- coding:utf-8 -*-

import unittest
class AssertIn_assertNotIn(unittest.TestCase):
    def setUp(self):
        print('test start')
    def test_assertin(self):
        a = 'hello'
        b = 'helloworld'
        self.assertIn(a,b,msg = 'a not in b')
    def test_assertnotin(self):
        c = 'abc'
        d = 'a'
        self.assertNotIn(d,c,msg = 'c in d')
    def tearDown(self):
        print('test end!')
if __name__ == '__main__':
    unittest.main()