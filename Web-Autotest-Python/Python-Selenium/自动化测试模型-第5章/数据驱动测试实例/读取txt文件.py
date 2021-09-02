#-*- coding:utf-8 -*-
with open('user_info',mode='r',encoding='utf-8') as file:
    lines = file.readlines()

for i in lines:
    username = i.strip().split(',')[0]
    password = i.strip().split(',')[1]
    print(username,password)


