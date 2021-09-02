# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/6/13 6:58
# @Software       : PyCharm
# @Python_verison : 3.7

# 1、python线程库
'''
python通过两个标准库thread和threading提供了对线程的支持，thread提供了低级别的、原始的线程和一个简单的锁，threading基于
java的线程模型设计。锁lock和条件变量condition在java中是对象的基本行为，每一个对象都自带了锁和条件变量，而在python则是独立的对象。
'''
# 2、threading模块
'''
我们应该避免使用thread模块，因为它不支持线程守护，当主线程停止工作时，所有的子线程不管在不在工作都会被强制退出，这时
就引入了守护线程的概念，threading支持守护线程，所以我们直接使用threading模块来修改上一节的例子。
'''
from time import sleep,ctime
import threading

# 播放音乐
def music(func,number):
    for i in range(number):
        print('i was listening %s,%s' %(func,ctime()))
        sleep(2)

# 播放电影
def movie(func,number):
    for i in range(number):
        print('i was at %s,%s' %(func,ctime()))
        sleep(5)

# 创建线程数组
threads = []

# 创建线程t1，并添加到线程数组
t1 = threading.Thread(target=music,args=('凤凰传奇',2))
threads.append(t1)

# 创建线程t2，并添加到线程数组
t2 = threading.Thread(target=movie,args=('肖申克的救赎',2))
threads.append(t2)

if __name__ == '__main__':
    # 启动线程
    for i in threads:
        i.start()
    # 守护线程
    for i in threads:
        i.join()            # 如果不启用join方法对每个线程做等待终止，那么在线程执行时候可能会去执行后面的代码，
    print('all end:%s'%(ctime()))

'''
i was listening 凤凰传奇,Thu Jun 13 09:05:19 2019
i was at 肖申克的救赎,Thu Jun 13 09:05:19 2019
i was listening 凤凰传奇,Thu Jun 13 09:05:21 2019
i was at 肖申克的救赎,Thu Jun 13 09:05:24 2019
all end:Thu Jun 13 09:05:29 2019
从上可知，两个线程（t1，t2）都是在同一时间执行，然后t1隔2s执行一次，t2隔5s执行一次。总的耗时是10s，说明了两个线程是同时执行，然后达到了并发操作。
'''