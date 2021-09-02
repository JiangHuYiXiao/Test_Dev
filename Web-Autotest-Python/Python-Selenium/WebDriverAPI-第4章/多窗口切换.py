#-*- coding:utf-8 -*-
# 有的时候在一个窗口进行操作时，点击链接会跳转到另一个新的窗口进行操作，WebDriver提供了switch_to.window()方法，
# 比如从百度首页跳转到百度注册页面
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')

# 获取百度首页搜索窗口句柄
search_window = driver.current_window_handle
driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()

# 获取百度注册首页的窗口句柄
register_window = driver.current_window_handle
# 获取当前所有的窗口
all_handels = driver.window_handles

# 进入注册窗口
for i in all_handels:
    if i !=search_window:
        driver.switch_to.window(i)
        print('进入注册窗口了')
        driver.find_element_by_css_selector('#TANGRAM__PSP_3__userName').send_keys('username')
        driver.find_element_by_css_selector('#TANGRAM__PSP_3__password').send_keys('password')
        time.sleep(2)
driver.quit()

'''
在本例中所涉及的新方法如下：

current_window_handle：获得当前窗口句柄。

window_handles：返回所有窗口的句柄到当前会话。

switch_to.window()：用于切换到相应的窗口，与上一节的switch_to.frame()类似，前者用于不同窗口的切换，后者用于不同表单之间的切换
'''