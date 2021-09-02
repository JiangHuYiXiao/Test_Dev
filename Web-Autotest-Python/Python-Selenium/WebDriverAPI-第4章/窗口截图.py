# -*- coding:utf-8 -*-
# 自动化用例是由程序去执行的，因此有时候打印的错误信息并不十分明确。
# 如果在脚本执行出错的时候能对当前窗口截图保存，那么通过图片就可以非常直观地看出出错的原因。
# WebDriver提供了截图函数get_screenshot_as_file()来截取当前窗口。
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
driver.get_screenshot_as_file('F:\\Python-Selenium\\WebDriverAPI-第4章\\baidu_img.png')
time.sleep(3)
driver.quit()
