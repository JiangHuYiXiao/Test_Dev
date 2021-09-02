#-*- coding:utf-8 -*-
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
pref = {'profile.default_content_settings.popups':0,'download.default_directory':'F:\\Python-Selenium'}
options.add_experimental_option('prefs',pref)
driver = webdriver.Chrome(executable_path='C:\\Users\Administrator\AppData\Local\Programs\Python\Python37\chromedriver.exe',chrome_options=options)
driver.implicitly_wait(10)
driver.get('http://www.firefox.com.cn/')
driver.find_element_by_link_text('立即下载').click()
time.sleep(4)
driver.quit()