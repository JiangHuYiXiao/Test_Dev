# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/6/28 8:57
# @Software       : Python-Selenium
# @Python_verison : 3.7

'''
selenium grid只提供了多系统、多浏览器的执行环境，selenium grid本身并不是提供并行的执行测试用例，这个我们前面已经反复讲过，
下面就通过演示使用多线程技术结合selenium grid实现分布式并行的执行测试用例。
'''
# 1、启动selenium server
# 在selenium server所在路径下启动selenium server服务
# java -jar selenium-server-standalone-2.53.0.jar
# 访问http://localhost:4444/grid/console可以查看到控制台信息

# 2、本机启动一个主hub，和一个node节点，端口号分别为4444,5555，本机ip地址为，172.20.49.38
# java -jar selenium-server-standalone-2.53.0.jar -role node port 5555

# 3、启动一个远程node节点：假设ip地址为172.187.28.1
# java -jar selenium-server-standalone-2.53.0.jar -role node port 6666
'''
远程node必须满足以下要求：
1、本地主机和远程主机必须能够ping通
2、远程主机必须安装用例执行的浏览器和驱动，并且驱动要放在path路径下
3、远程主机必须安装java环境，因为要运行selenium server
这里暂时不启动，因为资源不够、或者启用虚拟机
'''
from selenium import webdriver
from time import ctime,sleep
from threading import Thread

# 测试用例
def test_baidu(host,browser):
    print('test case start %s'%ctime())
    print(host,browser)
    dc = {'browser_name':browser}
    driver = webdriver.Remote(command_executor=host,desired_capabilities=dc)
    driver.get('http://www.baidu.com/')
    driver.find_element_by_css_selector('#kw').clear()
    driver.find_element_by_css_selector('#kw').send_keys(browser)
    driver.find_element_by_css_selector('#su').click()
    driver.quit()

if __name__ == '__main__':
    # 启动参数（启动参数和浏览器）
    dicts = {'http://127.0.0.1:4444/wd/hub':'Google Chrome',
             'http://127.0.0.1:5555/wd/node': 'Internet Explorer'
             }#远程节点  'http://172.187.28.1:6666/wd/node': 'firefox',
    threads = []
    # 创建线程
    for host,browser in dicts.items():
        t = Thread(target=test_baidu,args=(host,browser))
        threads.append(t)

    for i in threads:
        i.start()
    for i in threads:
        i.join()
    print('all case end %s'%ctime())