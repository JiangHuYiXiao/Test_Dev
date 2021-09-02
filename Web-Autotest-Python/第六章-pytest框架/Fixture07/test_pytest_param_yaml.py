# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/5/7 9:20
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
pytest,结合PyYAML可以对测试步骤、测试数据进行参数化（数据驱动）
'''
import pytest
import yaml
class TestDemo():
    @pytest.mark.parametrize("env",yaml.safe_load(open('./env.yml')))    #  参数后面的value必须是一个列表形式否则的话只能获取到参数名称，无法获取值，（yml的格式为字典）
                                                                           #  如果一定需要这样获取名称和值，则需要修改env.yml的格式为列表格式，
    def test_demo(self,env):
        if 'test' in env:
            print('这是测试环境')
            # print(env)      # 这样获取到的只是参数名称test
            # print(env)      # 修改yml文件的数据类型为列表后结果为{'test': '127.0.0.1'}
            print('环境ip为:',env['test'])
        elif 'dev' in env:
            print('这是开发环境')
            print('环境ip为:', env['dev'])





