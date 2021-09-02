# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/6/14 7:59
# @Software       : Python-Selenium
# @Python_verison : 3.7
# 除了直接使用pythonn自带的threadin、thread类我们还可以自己定义线程类根据自己的需求

import threading
from time import sleep,ctime

class Mythread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)         # 使用父类threading的Thread方法
        self.func = func
        self.args = args
        self.name = name
    def run(self):
        self.func(*self.args)           # *self._args 表示接受元组类参数；
def super_play(file,time):
    for i in range(2):
        print('start playing %s,%s'%(file,ctime()))
        sleep(time)

dict = {'霸王别姬.mp4':2,'青藏高原.mp3':3}
threads = []
for file,time in dict.items():
    t = Mythread(super_play,(file,time),super_play.__name__)
    threads.append(t)

if __name__ == '__main__':
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    print('all end %s' % (ctime()))

'''
start playing 霸王别姬.mp4,Tue Jun 18 07:29:14 2019
start playing 青藏高原.mp3,Tue Jun 18 07:29:14 2019
start playing 霸王别姬.mp4,Tue Jun 18 07:29:16 2019
start playing 青藏高原.mp3,Tue Jun 18 07:29:17 2019
all end Tue Jun 18 07:29:20 2019
'''
