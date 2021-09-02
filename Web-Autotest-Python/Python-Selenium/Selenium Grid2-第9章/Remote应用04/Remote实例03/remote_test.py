# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/6/11 7:20
# @Software       : PyCharm
# @Python_verison : 3.7
'''
from selenium.webdriver import Remote
# 调用remote方法
driver = Remote(command_executor = 'http://127.0.0.1:4444/wd/hub',desired_capabilities={'platform':'ANY',
                                                                                        'browserName':'chrome',
                                                                                        'verson':'',
                                                                                        'javascriptEnabled':'True'
                                                                                        }
                )
driver.get('http://www.baidu.com')
driver.find_element_by_css_selector('#kw').clear()
driver.find_element_by_css_selector('#kw').send_keys('remote')
driver.find_element_by_css_selector('#su').click()
driver.quit()
# 从上面的编写的代码来看就相当于我们使用webdriver.Chrome(),但是remote却大大增加了配置的灵活性，不同机子，不同浏览器配置。
'''

# 通过selenium server可以创建本地节点和远程节点，而remote的作用就是配置测试用例在这些节点上执行，下面演示两者的结合。

# 1、启动本机hub主节点
# java -jar selenium-server-standalone-3.8.0.jar -role hub

# 2、启动本机node分支节点
# java -jar selenium-server-standalone-3.8.0.jar -role node -port 5555
# java -jar selenium-server-standalone-3.8.0.jar -role node -port 5556

# 3、修改脚本使得其在不同的节点和浏览器使用
from selenium.webdriver import Remote
# 定义主机和浏览器
lists = {'http://127.0.0.1:4444/wd/hub':'chrome',
         'http://127.0.0.1:5555/wd/hub':'firefox',
         'http://127.0.0.1:5556/wd/hub':'internet explorer'
         }

# 定义不同的浏览器执行脚本
for host,broswer in lists.items():
    print(host,broswer)
    driver = Remote(command_executor=host,desired_capabilities={'platform':'ANY',
                                                                'browserName':'chrome',
                                                                'verson':'',
                                                                'javascriptEnabled':'True'
                                                                }
                    )
    driver.get('http://www.baidu.com')
    driver.find_element_by_css_selector('#kw').clear()
    driver.find_element_by_css_selector('#kw').send_keys('remote')
    driver.find_element_by_css_selector('#su').click()
    driver.quit()

# 启动远程node
# 我们现在的运行的脚本都是在本机上，要想在其他远程主机上运行node，必须满足下面的几个条件：
# 1、本地hub和远程node主机之间必须用ping命令连通
# 2、远程主机必须安装用例执行的驱动和浏览器，并且驱动要放在环境变量path目录下
# 3、远程主机必须安装java环境，因为需要运行selenium server
# 操作步骤：

# 1、启动本地主机（ip:172.0.0.1）
# java -jar selenium-server-standalone-3.8.0.jar -role hub
# 2、启动远程node主机，IP：172.1.12.24
# java -jar selenium-server-standalone-3.8.0.jar -role node -port 5555 -hub http://127.0.0.1:4444/grid/register
# 3、修改主机的ip地址和端口号，使其在internet explorer上运行
from selenium.webdriver import Remote
# 定义主机和浏览器
lists = {'http://127.0.0.1:4444/wd/hub':'chrome',
         'http://127.0.0.1:5555/wd/hub':'firefox',
         'http://172.1.12.24:5556/wd/hub':'internet explorer'
         }

# 定义不同的浏览器执行脚本
for host,broswer in lists.items():
    print(host,broswer)
    driver = Remote(command_executor=host,desired_capabilities={'platform':'ANY',
                                                                'browserName':'chrome',
                                                                'verson':'',
                                                                'javascriptEnabled':'True'
                                                                }
                    )
    driver.get('http://www.baidu.com')
    driver.find_element_by_css_selector('#kw').clear()
    driver.find_element_by_css_selector('#kw').send_keys('remote')
    driver.find_element_by_css_selector('#su').click()
    driver.quit()
# 4、运行脚本

# 在启动selenium server时，每次都需要输入长串的命令，可以将启动生成批处理文件，
# 首先创建一个startup.bat文件，selenium server路径为E:\Software Test\selenium-server-standalone-3.8.0
# 然后在bat文件中输入java -jar E:\Software Test\selenium-server-standalone-3.8.0.jar -role hub,
# 以后在需要启动selenium server时双击startup.up文件就可以
# 另外我们还可以通过VisGrid工具来启动和管理节点