# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/6/19 7:48
# @Software       : PyCharm
# @Python_verison : 3.7
'''
multiprocessing提供了threading中没有的IPC（进程间通信），效率上更高，应该优先考虑Pipe和Queue，
multiprocessing包中有Pipe类和Queue类分别支持者两种IPC机制,pipe和queue可以用来传递常见的对象，
Python 为进程通信提供了两种机制：
Queue：一个进程向 Queue 中放入数据，另一个进程从 Queue 中读取数据。
Pipe：Pipe 代表连接两个进程的管道。程序在调用 Pipe() 函数时会产生两个连接端，分别交给通信的两个进程，接下来进程既可从该连接端读取数据，也可向该连接端写入数据。
1、
pipe可以单向half_duplex也可以是双向duplex，我们通过multiprocessing.Pipe（duplex=False）创建单向管道，默认为双向
一个进程从pipe一端进入，被pipe的另一端接收，双向管道允许从两端输入。

'''
import multiprocessing

def proc1(a):
    a.send('hello')
    print('proc1 rec:',a.recv())
def proc2(a):
    a.send('hello,too')
    print('proc2 rec:',a.recv())
    # a.send('hello,too')


if __name__ == '__main__':
    multiprocessing.freeze_support()             # 在Windows下编译需要加这行
    pipe = multiprocessing.Pipe()                # 创建一个管道,返回两个连接端PipeConnection 对象,代表管道的两个连接端（一个管道有两个连接端，分别用于连接通信的两个进程）。

    P1 = multiprocessing.Process(target=proc1,args=(pipe[0],))      # 创建进程 P1
    P2 = multiprocessing.Process(target=proc2,args=(pipe[1],))      # 创建进程 P2
    P1.start()
    P2.start()
    P1.join()
    P2.join()

# P1进程通过PipeConnection向管道发送数据，数据将会被发送到管道的另一端的P2进程，通过recv方法接收，send方法发送
# P2进程通过PipeConnection向管道发送数据，数据将会被发送到管道的另一端的P1进程，通过recv方法接收，send方法发送
'''
PipeConnection 对象包含如下常用方法：
send(obj)：发送一个 obj 给管道的另一端，另一端使用 recv() 方法接收。需要说明的是，该 obj 必须是可 picklable 的（Python 的序列化机制），如果该对象序列化之后超过 32MB，则很可能会引发 ValueError 异常。
recv()：接收另一端通过 send() 方法发送过来的数据。
fileno()：关于连接所使用的文件描述器。
close()：关闭连接。
poll([timeout])：返回连接中是否还有数据可以读取。
send_bytes(buffer[, offset[, size]])：发送字节数据。如果没有指定 offset、size 参数，则默认发送 buffer 字节串的全部数据；如果指定了 offset 和 size 参数，则只发送 buffer 字节串中从 offset 开始、长度为 size 的字节数据。通过该方法发送的数据，应该使用 recv_bytes() 或 recv_bytes_into 方法接收。
recv_bytes([maxlength])：接收通过 send_bytes() 方法发迭的数据，maxlength 指定最多接收的字节数。该方法返回接收到的字节数据。
recv_bytes_into(buffer[, offset])：功能与 recv_bytes() 方法类似，只是该方法将接收到的数据放在 buffer 中。
'''
