# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/5/7 18:47
# @Software       : Python-Selenium
# @Python_verison : 3.7
# 现在我们每次运行的测试报告名称都是一样，这样会导致每次运行都会把上一次的报告文件覆盖掉，这样显然不好，
# 所以我们需要对测试报告的名称进行优化，比如在每次运行时测试报告文件=名称+运行时间
# python中的time模块提供了丰富的方法供我们使用
# time有三种格式
# 1、时间戳时间：timestamp 浮点数，从1970年1月1日 的00:00:00开始按照秒计时的偏移量，是一个浮点数，计算机读懂的时间
# 2、结构化时间：struct_time 元组类型，time.struct_time(tm_year=2019, tm_mon=1, tm_mday=8, tm_hour=19, tm_min=6, tm_sec=6, tm_wday=1, tm_yday=8, tm_isdst=0)，用于操作时间
# 3、格式化时间：format string 字符串类型，年-月-日 时:分:秒,是为了给人能够看的懂的时间
# 格式化时间的格式存在下面这些
'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''
'''
import time
timestamp = time.time()
print(timestamp)            # 1557226959.798

struct_time = time.localtime(timestamp)
print(struct_time)          # time.struct_time(tm_year=2019, tm_mon=5, tm_mday=7, tm_hour=19, tm_min=3, tm_sec=52, tm_wday=1, tm_yday=127, tm_isdst=0)

format_time = time.strftime('%Y-%m-%d %H:%M:%S',struct_time)
print(format_time)          # 2019-05-07 19:05:55
'''
import unittest
import time
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
class Test_baidu(unittest.TestCase):
    '''百度搜索测试'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.base_url = 'http://www.baidu.com'
        print('test baidu start')
    def test_baidu(self):
        '''搜索selenium关键字'''
        self.driver.get(self.base_url + '/')
        self.driver.find_element_by_css_selector('#kw').clear()
        self.driver.find_element_by_css_selector('#kw').send_keys('selenium')
        self.driver.find_element_by_css_selector('#su').click()
        time.sleep(5)
    def tearDown(self):
        self.driver.quit()
        print('test baidu end')

print(__name__)
if __name__ == '__main__':
    # 定义测试套件
    suite = unittest.TestSuite()
    # 套件中添加用例
    suite.addTest(Test_baidu('test_baidu'))
    # 获取格式化时间
    now_time = time.strftime('%Y-%m-%d %H_%M_%S')
    # 定义报告存放路径
    filename = './'+now_time + 'result.html'
    file = open(filename,'wb')
    runner = HTMLTestRunner(stream=file,title='百度搜索测试报告',description='用例执行情况:')
    # 运行测试用例
    runner.run(suite)
    # 关闭报告
    file.close()