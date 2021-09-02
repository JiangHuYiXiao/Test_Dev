#-*- coding:utf-8 -*-
'''
在WebDriver中处理JavaScript所生成的alert、confirm以及prompt十分简单，具体做法是使用 switch_to.alert
方法定位到 alert/confirm/prompt，然后使用text/accept/dismiss/ send_keys等方法进行操作。
text：返回 alert/confirm/prompt 中的文字信息。

accept()：接受现有警告框。

dismiss()：解散现有警告框。

send_keys(keysToSend)：发送文本至警告框。keysToSend：将文本发送至警告框。

如下图，百度搜索设置弹出的窗口是不能通过前端工具对其进行定位的，这个时候就可以通过switch_to_alert()方法接受这个弹窗。
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')
# 鼠标悬停到设置
move_element = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(move_element).perform()

# 打开搜索设置
driver.find_element_by_link_text('搜索设置').click()
time.sleep(2)

# 保存搜索设置
driver.find_element_by_css_selector("div#gxszButton>a.prefpanelgo").click()
time.sleep(2)

# 接受警告框
# driver.switch_to.alert().accept()   不对

alert = driver.switch_to.alert
print(alert.text)           # 已经记录下您的使用偏好
time.sleep(2)

# alert.send_keys('关闭')
# time.sleep(2)

alert.accept()
time.sleep(2)
# 退出
driver.quit()





