# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/7/10 7:25
# @Software       : PyCharm
# @Python_verison : 3.7
from selenium import webdriver
import os
'''
定义截图函数
为了保持自动化项目的可移植性，采用相对路径将测试截图保存到./report/image目录中
'''

def insert_img(driver,file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    '''
    base_dir1 = os.path.dirname((__file__))
    print(__file__)             # 返回脚本的绝对路径
    print(os.path.split(os.getcwd()))       # 将path分割成目录和文件名二元组返回 ('F:\\Python-Selenium\\自动化测试项目实战第11章\\BBS社区项目实战02\\mztestpro\\bbs\\test_case', 'models')
    print(base_dir1)            # 返回path的目录。其实就是os.path.split(path)的第一个元素
    print(base_dir)
    '''
    base_dir = str(base_dir).replace('\\','/')
    base = base_dir.split('/test_case')[0]
    file_path = base + '/report/image/'+ file_name
    driver.get_screenshot_as_file(file_path)
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    insert_img(driver,'baidu.jpg')
    driver.quit()

