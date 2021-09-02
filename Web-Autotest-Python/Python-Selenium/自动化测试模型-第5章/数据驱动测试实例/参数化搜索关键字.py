#-*- coding:utf-8 -*-
from selenium import webdriver
import time
search_text = ['python','NBA','轩逸']
for i in search_text:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('http://www.baidu.com')
    driver.find_element_by_css_selector('#kw').send_keys(i)
    driver.find_element_by_css_selector('#su').click()
    time.sleep(3)
    driver.quit()