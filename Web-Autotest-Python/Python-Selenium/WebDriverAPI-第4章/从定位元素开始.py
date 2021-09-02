# -*- coding:utf-8 -*-
# 测试版本

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(5)
driver.close()

# 1、id定位
# 由于HTML规定在一个html中所有元素的id是唯一的，所以，我们可以使用id唯一定位到一个元素
# 输入框： <input type="text" class="s_ipt nobg_s_fm_hover" name="wd" id="kw" maxlength="100" autocomplete="off">
# 搜索按钮：<input type="submit" value="百度一下" id="su" class="btn self-btn bg s_btn">
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_elements_by_id('su').click()
driver.quit()

# 2、name定位
# name在一个html中不一定唯一，所以不建议一般
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_name('wd').send_keys('selenium')
# 由于百度搜索框没有name所以不能用name定位
driver.quit()

# 3、class定位
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_class_name('s_ipt nobg_s_fm_hover').send_keys('selenium')
driver.find_element_by_class_name('bg btn self-btn bg s_btn').click()
driver.quit()

# 4、tag定位
# 一个html中的tag太多重复了，不建议
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_tag_name('input')
driver.quit()

# 5、link定位
# 使用文本链接来定位，利用的是标签对中的文本信息来定位
# <a href="http://news.baidu.com" target="_blank" class="mnav">新闻</a>
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_link_text('新闻').click()
driver.quit()

# 6、partial link定位
# 这个partial link定位是对link的一种补充，用于一些较长的文本链接，这时候我们可以取文本的一部分来进行定位
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baiu.com')
driver.find_element_by_partial_link_text('这是一个很长的链接').click()
driver.find_element_by_partial_link_text('这是一个').click()
driver.quit()

# 7、XPath定位 find_element_by_xpath
    # 绝对路径定位
# 百度输入框的绝对路径为：/html/body/div[2]/div[4]/div/div/div/form/span/input
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/span/input').send_keys('selenium')
driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/span[2]/input').click()
time.sleep(3)
driver.quit()

    # 利用元素属性定位
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_xpath("//*[@id='kw']").send_keys('selenium')   # *表示所有标签，也可以指明是哪个标签
driver.find_element_by_xpath("//input[@id = 'su']").click()
time.sleep(3)
driver.quit()

    # 层级和属性结合
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_xpath("//span[@class='bg s_ipt_wr']/input").send_keys('selenium')
driver.find_element_by_xpath("//span[@class='btn_wr s_btn_wr bg']/input").click()
time.sleep(2)
driver.quit()


    # 通过逻辑运算符
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_xpath("//span[@class='bg s_ipt_wr' and @id = 's_kw_wrap']/input").send_keys('selenium')
driver.find_element_by_xpath("//span[@class='s_btn_wr bg' and @id = 's_btn_wr']/input").click()
driver.quit()

# 8、css定位


# 8、css定位
# 1、通过css属性定位
# <input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">
# <input type="submit" value="百度一下" id="su" class="btn self-btn bg s_btn btn_h btnhover">
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_css_selector('.s_ipt').send_keys('selenium')
driver.find_element_by_css_selector('.bg s_btn').click()
time.sleep(2)
driver.quit()

# 2、通过id属性定位
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_css_selector('#kw').send_keys('selenium')
driver.find_element_by_css_selector('#su').click()
time.sleep(2)
driver.quit()

# 3、通过标签名定位
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# 父子关系
# driver.find_element_by_css_selector('span>input').send_keys('selenium')
# # 属性定位
# driver.find_element_by_css_selector('[autocomplete="off"]').send_keys('selenium')
# 组合定位---推荐
driver.find_element_by_css_selector('form.fm>span#s_kw_wrap>input[autocomplete="off"]').send_keys('selenium')
driver.find_element_by_css_selector('form#form>span#s_btn_wr>input[type="submit"]').click()
time.sleep(2)
driver.quit()

