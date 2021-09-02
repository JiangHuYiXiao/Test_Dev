# -*- coding:utf-8 -*-
# 虽然webdriver提供了操作浏览器的方法，但是对于浏览器的滚动条并没有提供相应的方法，在这种情况下就可以借助javasc来控制浏览器的滚动条。
# webdriver提供了execute_script()方法来执行javasript脚本
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')

# 点击
driver.find_element_by_css_selector('#kw').send_keys('window.scrollTo()')
driver.find_element_by_css_selector('#su').click()
time.sleep(3)
# 将页面滚动条拖动到底部
js1 = 'document.documentElement.scrollTop=10000'
driver.execute_script(js1)
time.sleep(3)
# 将页面滚动条拖动到顶部
js2 = 'document.documentElement.scrollTop=0'
driver.execute_script(js2)
# 设置浏览器大小
driver.set_window_size(500,500)
# 通过js控制浏览器窗口的滚动条的位置
js = 'window.scrollTo(100,700);'
# 调用js
driver.execute_script(js)
time.sleep(5)
driver.quit()

# 通过浏览器打开百度进行搜索，并且提前通过set_window_size()方法将浏览器窗口设置为固定宽高显示，目的是让窗口出现水平和垂直滚动条。
# 然后通过execute_script()方法执行JavaScripts代码来移动滚动条的位置。
'''

# 示例二：
# 一般在web端的时间控件，都是readonly属性的，这种标签的话selenium是无法定位操作的，只能查看，所以，遇到这种情况我们需要使用javascript进行操作。
# 首先，将readonly属性删除。
# 其次，赋值一个value
from selenium import webdriver
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_datetime():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.12306.cn/index/')
        # self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_datetime(self):
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        sleep(4)
        self.driver.execute_script("document.getElementById('train_date').value='2021-01-06'")
        sleep(3)

        print(self.driver.execute_script("return document.getElementById('train_date').value"))





