#-*- coding:utf-8 -*-
# 1、控制浏览器窗口大小
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://mail.10086.cn')
print('设置浏览器的宽为480，高为800')
driver.set_window_size(480,800)
time.sleep(2)
driver.quit()

# 最大
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://mail.10086.cn')
driver.maximize_window()
time.sleep(3)
driver.quit()

# 2、控制浏览器前进后退----一般直接用get就可以
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
print(driver.current_url)

driver.find_element_by_link_text('新闻').click()
print(driver.current_url)

# 后退
driver.back()
print(driver.current_url)

# 前进
driver.forward()
print(driver.current_url)
'''

# https://www.baidu.com/
# http://news.baidu.com/
# https://www.baidu.com/
# http://news.baidu.com/

# 3、登录163邮箱

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://mail.163.com')
# time.sleep(9)
driver.implicitly_wait(5)           # 等待超时的时间
# 切换 iframe：
# 1.由于登录按钮是在iframe上，所以第一步需要把定位器切换到iframe上
iframe_id = driver.find_element_by_css_selector('div#loginDiv>iframe')
driver.switch_to.frame(iframe_id)

# 2、清除label信息
# 用户名
driver.find_element_by_css_selector('.j-inputtext.dlemail').clear()
driver.find_element_by_css_selector('.j-inputtext.dlemail').send_keys('18270717374')

# 密码
driver.find_element_by_css_selector('.j-inputtext.dlpwd').clear()
driver.find_element_by_css_selector('.j-inputtext.dlpwd').send_keys('jiangtao0313')
# 登录
driver.find_element_by_css_selector('#dologin').click()
time.sleep(2)
driver.maximize_window()
# 退出iframe
driver.switch_to.default_content()
driver.quit()

# 4、submit()
# submit()的功能和click类似，但是click的功能更强大，只能用于表单的提交和点击


# 5、刷新当前页面
driver.refresh()