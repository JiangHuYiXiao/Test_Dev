# -*- coding:utf-8 -*-
# WebDriver还提供了8种用于定位一组元素的方法。与定位元素不同的是，这些element加了s为elements。
# 1、driver.find_elements_by_id('kw')
# 2、driver.find_elements_by_name('wd')
# 3、driver.find_elements_by_class_name('s_ipt')
# 4、driver.find_elements_by_tag_name('input')
# 5、driver.find_elements_by_link_text('新闻')
# 6、driver.find_elements_by_partial_link_text('新')
# 7、driver.find_elements_by_xpath('//*[@id="kw"]')
# 8、driver.find_elements_by_css_selector('#kw')
# driver.find_elements_by_tag_name()

# 1、使用标签名

from selenium import webdriver
import time
import os
file_path = (os.path.abspath('checkbox.html'))
driver = webdriver.Chrome()
driver.get(file_path)
inputs = driver.find_elements_by_tag_name('input')
for i in inputs:
    if i.get_attribute('type')=='checkbox':
        i.click()
        time.sleep(2)


# 2、使用find_elements_by_css_selector 、find_elements_by_xpath定位方法
from selenium import webdriver
import time
import os
file_path = (os.path.abspath('checkbox.html'))
driver = webdriver.Chrome()
driver.get(file_path)
inputs = driver.find_elements_by_css_selector("input[type='checkbox']")     # find_elements_by_css_selector进行定位

# driver.find_elements_by_xpath("//input[@type='checkbox']")   find_elements_by_xpath进行定位
for i in inputs:
    i.click()
    time.sleep(2)

# 3、统计同类型的元素有多少个
print(len(inputs))

# 4、只勾选第一个和第三个
from selenium import webdriver
import time
import os
file_path = (os.path.abspath('checkbox.html'))
driver = webdriver.Chrome()
driver.get(file_path)
driver.find_elements_by_xpath("//input[@type='checkbox']").pop(0).click()   # find_elements_by_xpath进行定位
time.sleep(2)
driver.find_elements_by_xpath("//input[@type='checkbox']").pop(2).click()
time.sleep(2)
driver.quit()