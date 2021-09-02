# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
'''
以下为常用的键盘操作：
send_keys(Keys.BACK_SPACE) 删除键（BackSpace）

send_keys(Keys.SPACE) 空格键(Space)

send_keys(Keys.TAB) 制表键(Tab)

send_keys(Keys.ESCAPE) 回退键（Esc）

send_keys(Keys.ENTER) 回车键（Enter）

send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）

send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）

send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）

send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）

send_keys(Keys.F1) 键盘 F1

……

send_keys(Keys.F12) 键盘 F12
'''
driver  = webdriver.Chrome()
driver.get('https://www.baidu.com')
# 输入
driver.find_element_by_css_selector('#kw').send_keys('seleniumm')
time.sleep(2)
# 删除
driver.find_element_by_css_selector('#kw').send_keys(Keys.BACKSPACE)
time.sleep(2)
#输入空格+教程
driver.find_element_by_css_selector('#kw').send_keys(Keys.SPACE)
driver.find_element_by_css_selector('#kw').send_keys('教程')
time.sleep(2)
# 全选
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'a')
time.sleep(2)
# 剪切
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'x')
time.sleep(2)
# 复制
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'c')
time.sleep(2)
# 利用Enter代替单机操作
driver.find_element_by_css_selector('#kw').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_css_selector('#kw').send_keys(Keys.F12)
time.sleep(2)
driver.quit()


