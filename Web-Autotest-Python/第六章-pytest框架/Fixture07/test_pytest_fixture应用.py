# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/8/19 10:22
# @Software       : Python_study
# @Python_verison : 3.7

# 应用1：
    # 在执行测试用例之前的需要的操作可以封装到一个函数中，然后在该函数上面标记@pytest.fixture(),fixture默认的scope=function
import pytest



# @pytest.fixture()
def login():
    '''
    登录功能
    :return:None    #没有return时是返回None，有return就返回对应的值
    '''
    print('登录系统')
    user = 'jianguyixiao'
    return user
login()
class Test_Fixture():
    def test_case1(login):
        '''
        测试用例test_case1
        :return:
        '''
        print('test_case1','{}登录成功'.format(login()))


    def test_case2(self):
        '''
        测试用例test_case2
        :return:
        '''
        print('test_case2','不需要登录')
    def test_case3(login):
        '''
        测试用例test_case3
        :return:
        '''
        print('test_case3','{}登录成功'.format(login()))
'''
参数解析
fixture(scope="function", params=None, autouse=False,ids=None, name=None):
scope 有四个级别参数：function, class、Module、session
params: 一个可选的参数列表，它将导致多个参数调用fixture 功能和所有测试使用它。

autouse: 如果为 True，则为所有测试激活 fixture func 可以看到它。 如果为 False（默认值）则显式需要参考来激活 fixture
ids:每个字符串 id 的列表，每个字符串对应于 params 这样他们就是测试 ID 的一部分。 如果没有提供 ID 它们将从 params 自动生成。
name: fixture 的名称,这默认为装饰函数的名称

'''
# 不带参数时默认 scope="function"
@pytest.fixture()               # function，运行两次
def login():
    print("输入账号，密码先登录")
def test_s1(login):
    print("用例 1：需要登录操作")
def test_s2(login):         # 调用login，然后执行login（）
    print("用例 2：登录之后其它动作")


@pytest.fixture(scope="module")                 # 只运行一次
def open():
    print("打开浏览器，并且打开百度首页")

def test_s3(open):
    print("用例 1：搜索 python-1")

def test_s4(open):
    print("用例 2：搜索 python-2")


if __name__ == '__main__':
    pytest.main()