# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/6/20 8:54
# @Software       : Python-Selenium
# @Python_verison : 3.7

'''
queue类和pipe类相似，都是先进先出的模式，但是queue允许多个进程进入，多个进程从队列中取出对象，
queue类使用queue（maxsize）创建，maxsize表示存放对象的最大值
multiprocessing 模块下的 Queue 和 queue 模块下的 Queue 基本类似，它们都提供了 qsize()、empty()、full()、put()、put_nowait()、get()、get_nowait() 等方法。
区别只是 multiprocessing 模块下的 Queue 为进程提供服务，而 queue 模块下的 Queue 为线程提供服务。

'''
import multiprocessing
import os,time

def inputQ(queue):
    info = str(os.getpid())+ 'put:'+str(time.time())   # os.getpid()获取进程id
    queue.put(info)

def outputQ(queue,lock):
    info = queue.get()
    lock.acquire()          # 上锁
    print((str(os.getpid())+ 'get:'+info))              # os.getpid()获取进程id
    lock.release()          # 解锁


if __name__ == '__main__':
    record1 = []
    record2 = []
    lock = multiprocessing.Lock()           # 枷锁，为了防止散乱的打印
    queue = multiprocessing.Queue(3)            # 表示3个进程对象，最多支持3个

    for i in range(10):
        process = multiprocessing.Process(target=inputQ,args=(queue,))
        process.start()
        record1.append(process)
    for i in range(10):
        process = multiprocessing.Process(target=outputQ,args=(queue,lock))
        process.start()
        record2.append(process)
    for p in record1:
        p.join()
        queue.close()       # 没有更多对象进来，关闭queue
    for p in record2:
        p.join()