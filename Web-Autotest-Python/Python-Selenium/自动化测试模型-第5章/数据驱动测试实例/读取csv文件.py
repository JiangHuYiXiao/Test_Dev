# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/4/13 10:39
# @Software       : Python-Selenium
# @Python_verison : 3.7
'''
假设我们要从文件读取一个用户的用户名、密码、年龄、国家、性别等一组信息，如果这样我们再一个一个从txt文件中读取，
这样显然是比较麻烦的，对于这样数据，我们可以通过csv文件来存放。
'''
# 1、通过excel创建文件，另存为csv文件格式
# 导入csv包
import csv
# 读取csv_info文件
file = csv.reader(open('csv_info.csv',mode='r',encoding='utf-8'))
# 读取csv的所有数据
for i in file:
    print(type(i),i)
    print(i[0])     # 姓名
