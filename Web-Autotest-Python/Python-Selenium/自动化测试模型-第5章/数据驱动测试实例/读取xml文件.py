# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/4/13 11:08
# @Software       : Python-Selenium
# @Python_verison : 3.7
'''
有时候我们读取的数据是不规则的，例如我们需要一个配置文件来配置当前自动化测试脚本的url、浏览器、登录的用户名、密码等，这个时候就可以考虑用xml来存放这些信息。
xml文件一般用户数据传输，注重数据的内容，html用户数据的结构，显示。
xml的特点：
    xml也是标签对，但是这些标签对是可以自己配置<jt></jt>
    xml也是有属性的，<shuxing abc=123>
    xml标签对中可以放文本<>穷<>
    xml标签也可以表示层级关系
    <father>
        <sun></sun>
'''
from xml.dom import minidom
# d打开xml文档
dom = minidom.parse('info.xml')
# 得到文档于元素对象
root = dom.documentElement
print(root.nodeName,root.nodeValue,root.nodeType,root.ELEMENT_NODE)         # info None 1 1
# 获取任意标签名
login_name = root.getElementsByTagName('login')     # login
print(login_name[0].tagName)            # login
maxid_name = root.getElementsByTagName('maxid')
print(maxid_name[0].tagName)            # maxid
caption_name = root.getElementsByTagName('caption')
print(caption_name)             # [<DOM Element: caption at 0x1fd5f20>, <DOM Element: caption at 0x20640e0>, <DOM Element: caption at 0x2064210>]
print(caption_name[0].tagName)          # caption
print(caption_name[1].tagName)          # caption

# 获得标签的属性值
user_name = login_name[0].getAttribute('username')
pass_word = login_name[0].getAttribute('password')
print(user_name,pass_word)              # pytest 123456

# 获取第一、二个item的id属性
item_name = root.getElementsByTagName('item')
item_id1 = item_name[1].getAttribute('id')
item_id = item_name[0].getAttribute('id')
print(item_name[1].tagName,item_id1)
print(item_name[0].tagName,item_id)


# 获得标签对之间的数据
data0 = caption_name[0].firstChild.data
data1 = caption_name[1].firstChild.data
data2 = caption_name[2].firstChild.data

print(data0,data1,data2)



