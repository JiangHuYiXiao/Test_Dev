# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/6/18 7:33
# @Software       : PyCharm
# @Python_verison : 3.7
'''
多进程multiprocessing模块的使用和多线程threading模块的用法类似，multiprocessing提供了本地和远程的并发性，
有效的通过全局解释锁（GIL）来使用进程，由于GIL的存在，在CPU密集型的程序中，使用多线程并不能有效的利用多核CPU的优势，
因为一个解释器在同一时刻，只会有一个线程在执行，所以，multiprocessing模块可以充分利用硬件的多处理器来进行工作，
它支持unix和windows系统上的运行。
'''
from time import sleep,ctime
import multiprocessing

def super_play(file,time):
    for i in range(2):
        print('playing start %s,%s'%(file,ctime()))
        sleep(time)

dict = {'霸王别姬.mp4':3,'一万个可能.mp3':2}
lists = []

for file,time in dict.items():
    t = multiprocessing.Process(target=super_play,args=(file,time))
    lists.append(t)

if __name__ == '__main__':
    for i in lists:
        i.start()
    for i in lists:
        i.join()            # 等待线程终止
    print('all end %s'%ctime())

'''
playing start 霸王别姬.mp4,Wed Jun 19 07:39:08 2019
playing start 一万个可能.mp3,Wed Jun 19 07:39:08 2019
playing start 一万个可能.mp3,Wed Jun 19 07:39:10 2019
playing start 霸王别姬.mp4,Wed Jun 19 07:39:11 2019
all end Wed Jun 19 07:39:14 2019
'''
# 从上面执行的结果可以看出，多进程和多线程的结果是一样的，看不出来他们有啥差异，
# 我们利用multiprocessing中的Process创建进程，
# 进程中也有start，join方法
# Process类初始化参数有(self, group=None, target=None, name=None, args=(), kwargs={})
# target 表示调用对象
# group 基本不用
# name 别名
# args 位置参数
# kwargs 字典参数
