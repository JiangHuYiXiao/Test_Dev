# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/6/1 8:00
# @Software       : PyCharm
# @Python_verison : 3.7
'''
selenium grid用于设计帮助我们进行分布式测试的工具，其整个结构由一个hub主节点和多个node代理节点组成。
hub主节点用于管理各个代理节点的状态和注册信息的，并且接收远程客户端代码的请求调用，然后把请求的命令再转发给各个
代理节点来执行，使用grid远程执行测试代码和直接调用selenium server是一样的，只是环境启动的方式不一样，直接调用selenium server
就是启动server就好，使用grid远程执行就需要同时启用一个hub和至少一个node代理节点。
'''
# 启动一个hub
# java -jar selenium-server-standalone-3.8.0.jar -role hub  默认端口是4444
# 启动一个node
# java -jar selenium-server-standalone-3.8.0.jar -role node 默认端口是5555

# 如果一个主机上启用了多个node，则需要设置不同的端口号
# 比如
# java -jar selenium-server-standalone-3.8.0.jar -role node -port 5555
# java -jar selenium-server-standalone-3.8.0.jar -role node -port 5556
# java -jar selenium-server-standalone-3.8.0.jar -role node -port 5557
'''
当你的测试用例需要在多个环境验证时，可以并行的执行这些测试用例进而缩短测试总时间，并行的能力需要借助于编程语言的多线程技术
下一章我们将学习python的多线程技术，grid可以根据用例中指定的平台配置信息把用例转发给符合匹配要求的node测试代理。
'''
# 通过：http://127.0.0.1:4444/grid/console可以查看到控制台启动的节点信息