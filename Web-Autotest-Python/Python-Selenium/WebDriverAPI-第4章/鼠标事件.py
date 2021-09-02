# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
#导入鼠标事件操作的类ActionChains
from selenium.webdriver.common.action_chains import ActionChains

# 1、右击 context_click()
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

right_click = driver.find_element_by_css_selector('#su')
ActionChains(driver).context_click(right_click).perform()           # perform()执行所有 ActionChains 中存储的行为可以理解成是对整个操作的提交动作
sleep(3)

# 2、双击 double_click()

# 3、悬停 move_to_element()
# move_to_element = driver.find_element_by_css_selector('')
move_to_element = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(move_to_element).perform()
sleep(3)

# 4、鼠标拖动 drag_and_drop(被拖动的元素，拖动后的元素)
address_top = driver.find_element_by_css_selector('xxx')
address_behind = driver.find_element_by_css_selector('xxx')
ActionChains(driver).drag_and_drop(address_top,address_behind).perform()