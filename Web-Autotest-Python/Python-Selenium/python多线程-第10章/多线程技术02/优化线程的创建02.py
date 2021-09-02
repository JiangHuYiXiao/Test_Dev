# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/6/13 9:08
# @Software       : Python-Selenium
# @Python_verison : 3.7

'''
从上面的例子我们可以知道我们可以通过threading模块执行多线程，但是创建线程的方式太麻烦了，每创建一个线程需要使用:创建线程数组、创建线程t1、添加线程到线程数组
threads=[]
t1 = threading.Thread（target=object，args=（））
threads.append()
下面我们通过方法进行改进
'''
from time import ctime,sleep
import threading

# 定义一个超级播放器类
def super_player(file,time):
    for i in range(2):
        print('start playing %s,%s'%(file,ctime()))
        sleep(time)

# 定义一个字典存在播放的文件和播放时长
dict = {'一百万个可能.mp3':2,'山楂树之恋.mp4':2,'Fire.mp3':4}
length = range(len(dict))


# 创建线程数组
threads = []
for file,time in dict.items():
    t = threading.Thread(target=super_player,args=(file,time))
    threads.append(t)

if __name__ == '__main__':
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    print('all end %s'%(ctime()))

'''
start playing 一百万个可能.mp3,Thu Jun 13 09:55:27 2019
start playing 山楂树之恋.mp4,Thu Jun 13 09:55:27 2019
start playing Fire.mp3,Thu Jun 13 09:55:27 2019
start playing 一百万个可能.mp3,Thu Jun 13 09:55:29 2019
start playing 山楂树之恋.mp4,Thu Jun 13 09:55:29 2019
start playing Fire.mp3,Thu Jun 13 09:55:31 2019
all end Thu Jun 13 09:55:35 2019
总耗时8s，并发时耗时用最长的'Fire.mp3':4
'''