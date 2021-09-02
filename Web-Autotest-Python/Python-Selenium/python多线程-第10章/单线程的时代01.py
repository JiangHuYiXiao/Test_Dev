# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/6/12 7:29
# @Software       : PyCharm
# @Python_verison : 3.7
'''
在第9章我们已经学习了selenium grid，学习了分布式的运行测试用例，但是却没有学习到同时运行，也就是并行，并发运行。
并行和分布式是不一样的概念，
分布式：是指将一个测试用例远程调用到不同的环境下执行，
并行：强调的是同时执行多个任务。
在计算机中一般是使用多进程或者多线程来实现并发操作。
'''
# 什么是进程？
# 计算机程序只不过是磁盘中可执行的二进制数据，他们只有在被读取到内存中、被操作系统调用时才开始他们的生命周期。
# 进程是程序的一次执行，每个进程都有自己的空间、内存地址、数据栈等，操作系统管理在其上的所有进程，并为这些进程合理的分配时间。
# 比如说我们打开chrome浏览器就是一个进程

# 什么是线程？
# 线程和进程有点相似，都有自己的空间，地址、数据栈，但是所有的线程都是运行在一个进程中，可以将线程看做是一个迷你的进程，
# 比如说我们打开chrome浏览器观看视频、看网页、听歌，这些都是线程都运行在chrome这个进程中。

# 在单线程的时，处理器需要处理多个任务时，必须对这些任务安排执行顺序，假如我们创建二个任务
# 听歌，看电影，在单线程时，我们只能按照先后顺序来执行这两个任务
'''
from time import sleep,ctime

# 听歌
def music():
    print('i was listening to music %s' % ctime())
    sleep(2)

# 看电影
def movie():
    print('i was at the movie %s' % ctime())
    sleep(5)

if __name__ =='__main__':
    music()
    movie()
    print('all end:',ctime())

i was listening to music Wed Jun 12 07:53:58 2019
i was at the movie Wed Jun 12 07:54:00 2019
all end: Wed Jun 12 07:54:05 2019
从上可知，听歌任务运行2s，看电影运行5s，总共运行7s
'''
# 对上面的例子进行调整
# 用户希望在看电影和听歌之间进行切换，播放任意的电影和音乐，并且希望提供循环的功能，尤其对于音乐播放来说这是一个很重要的功能。
from time import sleep,ctime

# 听歌
def music(file,number):
    for i in range(number):
        print('i was listenting to %s,%s' % (file,ctime()))
        sleep(2)
# 看电影
def movie(file,number):
    for i in range(number):
        print('i was at %s ,%s' % (file,ctime()))
        sleep(5)
if __name__ == '__main__':
    music('十八岁的天空',3)
    movie('复仇者联盟4',5)
    print('all end %s' % ctime())

'''
i was listenting to 十八岁的天空,Wed Jun 12 08:08:51 2019
i was listenting to 十八岁的天空,Wed Jun 12 08:08:53 2019
i was listenting to 十八岁的天空,Wed Jun 12 08:08:55 2019
i was at 复仇者联盟4 ,Wed Jun 12 08:08:57 2019
i was at 复仇者联盟4 ,Wed Jun 12 08:09:02 2019
i was at 复仇者联盟4 ,Wed Jun 12 08:09:07 2019
i was at 复仇者联盟4 ,Wed Jun 12 08:09:12 2019
i was at 复仇者联盟4 ,Wed Jun 12 08:09:17 2019
all end Wed Jun 12 08:09:22 2019
这样就达到了循环听歌和循环看电影，按照用户的需求，在单线程就只能这样执行任务，先后执行
'''