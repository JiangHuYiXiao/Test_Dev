#-*- coding:utf-8 -*-
# 由于大多数web页面都存在ajax请求，所以当浏览器加载页面时，有的请求还在后台处理中，
# 这样就会元素没有显示，导致定位不了元素，自动化用例执行失败。
# webdriver提供了等待来改善这种问题，有显示等待和隐式等待。
'''
# 1、显示等待：指的是等待某个条件成立时继续执行，否则在达到最大时长时抛出超时异常（TimeoutException）
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait             # 显示等待
from selenium.webdriver.support import expected_conditions          # 异常处理
# import selenium.webdriver.support.expected_conditions as EC       这样也是可以导入的

driver = webdriver.Chrome()
driver.get('https://baidu.com')
WebDriverWait(driver,2,0.5).until(lambda x:x.find_element_by_css_selector('#kw')).send_keys('selenium')

is_disappeared = WebDriverWait(driver,4,0.5).until_not(lambda x:x.find_element_by_css_selector('#kw'))   # 显示则报TimeoutException，不显示则执行输出False
print(is_disappeared)
driver.quit()


WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
driver ：浏览器驱动。
timeout ：最长超时时间，默认以秒为单位。
poll_frequency ：检测的间隔（步长）时间，默认为0.5S。
ignored_exceptions ：超时后的异常信息，默认情况下抛NoSuchElementException异常。
WebDriverWait()一般由until()或until_not()方法配合使用，下面是until()和until_not()方法的说明。

until(method, message=‘’)
调用该方法提供的驱动程序作为一个参数，直到返回值为True。
until_not(method, message=‘’)
调用该方法提供的驱动程序作为一个参数，直到返回值为False。
'''
# 2、隐式等待
# WebDriver提供了implicitly_wait()方法来实现隐式等待，默认设置为0。它的用法相对来说要简单得多。
# 针对的是一个脚本中的所有元素，如果执行到某个元素没有显示，则一直循环执行，直到超过了设置的等待时间报异常，执行到第二个元素时也是一样的循环。。。
# 定位不到，或者定位时间长，则等待较长，使用这个隐式等待
from selenium import webdriver
from time import ctime
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.implicitly_wait(10)          # 等待十秒

try:
    print(ctime())          # 当前时间
    driver.find_element_by_css_selector('#kws').send_keys('selenium')
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
driver.quit()

# 结果
'''
Wed Mar 27 19:23:42 2019
Message: no such element: Unable to locate element: {"method":"css selector","selector":"#kws"}
  (Session info: chrome=73.0.3683.86)
  (Driver info: chromedriver=73.0.3683.68 (47787ec04b6e38e22703e856e101e840b65afe72),platform=Windows NT 6.1.7601 SP1 x86_64)

Wed Mar 27 19:23:52 2019
'''
# 3、使用sleep进行休眠