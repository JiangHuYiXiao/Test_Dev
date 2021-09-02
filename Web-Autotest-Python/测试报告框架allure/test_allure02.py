# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/8/17 9:00
# @Software       : Python_study
# @Python_verison : 3.7
import pytest
import allure_pytest
import allure

def test_case1():
    print('test_case1')

@pytest.mark.skip
def test_case2():
    print('test_case2')

def test_case3():
    print('test_case3')

def test_case4():
    print('test_case4')
    assert False

if __name__ == '__main__':
    pytest.main()


# allure generate ./report/3 -o ./reports/html --clean



# allure报告生成、查看
# 方法1
    # 1、使用：pytest 测试文件 --alluredir=./report/1                  ---生成测试报告
    # 2、要在测试完成后查看实际报告，您需要使用allure serve / tmp / my_allure_results命令生成报告，然后默认使用默认浏览器打开报告。   ----查看测试报告

# 方法2：
# 如果需要手动查看测试报告则需要：
    # 1、pytest 测试文件 --alluredir=./report/1                 ---生成测试报告
    # 2、allure generate F:\Python_study\Web-Autotest-Python\测试报告框架allure\report\1(测试报告) -o ./report/result --clean          ----查看测试报告
