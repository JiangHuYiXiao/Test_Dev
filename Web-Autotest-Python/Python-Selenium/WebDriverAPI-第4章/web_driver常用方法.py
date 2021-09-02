# -*- coding:utf-8 -*-

# 1、send.key(value)  输入

# 2、clear()         清除

# 3、click()         点击

# 4、refresh()       刷新页面
# 5、quit()          退出关闭浏览器

# 6、设置浏览器尺寸
# driver.set_window_size(480,800)
# 最大
# driver.maximize_window()

# 7、切换定位器到iframe
# driver.switch_to.frame('value')

# 8、退出定位器
# driver.switch_to.default_content()

# 9、size获取输入框的尺寸
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# size = driver.find_element_by_css_selector('#kw').size
# print(size)         # {'height': 22, 'width': 500}

# 10、获取文本信息
info = driver.find_element_by_css_selector('#cp').text
print(info)         # ©2019 Baidu 使用百度前必读 意见反馈 京ICP证030173号  京公网安备11000002000001号

# 11、获取元素属性值get_attribute()
attribute = driver.find_element_by_css_selector('#kw').get_attribute('maxlength')           # 255
attribute1 = driver.find_element_by_css_selector('#kw').get_attribute('class')          # s_ipt
attribute1 = driver.find_element_by_css_selector('#su').get_attribute('type')          # s_ipt
print(attribute,attribute1)

# 12、查看改元素用户是否可见is_displayed()
res = driver.find_element_by_css_selector('#su').is_displayed()
if res == True:
    driver.find_element_by_css_selector('#su').click()

driver.quit()