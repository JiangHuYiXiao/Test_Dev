#-*- coding:utf-8 -*-
# 验证用例的预期结果和实际结果是否一致，通常我们可以通过title、url、text方法进行验证
# text:获取标签对之间的文本信息
# url：获取当前页面的url
# title：获取当前页面的标题

# 例子：登录163邮箱
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://mail.163.com')
driver.implicitly_wait(5)
# 获取iframe的元素位置
iframe_id = driver.find_element_by_css_selector('div.loginUrs>iframe')
# 切换到iframe
driver.switch_to.frame(iframe_id)


# 清除输入框信息
driver.find_element_by_css_selector('.j-inputtext.dlemail').clear()
# 键盘输入
driver.find_element_by_css_selector('.j-inputtext.dlemail').send_keys('18270717374')


# 清除输入框信息
driver.find_element_by_css_selector('.j-inputtext.dlpwd').clear()

# 键盘输入
driver.find_element_by_css_selector('.j-inputtext.dlpwd').send_keys('jiangtao0313')

# 登录
driver.find_element_by_css_selector('#dologin').click()
# 验证登录成功

# 控制浏览器
driver.maximize_window()
time.sleep(2)

# text
user = driver.find_element_by_css_selector('#spnUid').text
print(user)
time.sleep(2)
# url
now_url = driver.current_url
print(now_url)
time.sleep(2)
# title
title = driver.title
print(title)
driver.quit()