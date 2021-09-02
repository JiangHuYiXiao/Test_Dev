#-*- coding:utf-8 -*-
# 有时我们会碰到下拉框，WebDriver提供了Select类来处理下拉框
# Select类用于定位select标签。
# select_by_value() 方法用于定位下接选项中的value值。
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('F:\Python-Selenium\WebDriverAPI\select处理下拉框.html')
# 实例化一个Select类对象
se = Select(driver.find_element_by_css_selector('#selectdemo'))

# 1、下面三种方法用于选择"篮球运动员"
se.select_by_index("2")         # 通过索引查找
se.select_by_value('210103')            # 通过value属性值查找
se.select_by_visible_text('篮球运动员')          # 通过标签显示的text查找

# 2、取消选中
se.deselect_all()
se.deselect_by_index("2")
se.deselect_by_value("210103")
se.deselect_by_visible_text('篮球运动员')

# 3、先定位select再定位option
se1 = driver.find_element_by_css_selector('#selectdemo')
se1.find_element_by_css_selector('[name="lanqiu"]').click()

# 4、直接定位
driver.find_element_by_xpath('//*[@id="selectdemo"]/option[3]').click()
