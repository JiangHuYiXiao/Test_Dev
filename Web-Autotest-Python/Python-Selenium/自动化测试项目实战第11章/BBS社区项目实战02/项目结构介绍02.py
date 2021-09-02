# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/7/8 7:41
# @Software       : PyCharm
# @Python_verison : 3.7
# 项目结构

'''
mztestpro/
    |---bbs/
    |   |---data/
    |   |---report/
    |   |   |---image/
    |   |---test_case/
    |       |---models
    |       |   |---driver.py
    |       |   |---function.py
    |       |   |---myunit.py
    |       |---page_obj.py/
    |       |   |---*base.py/
    |       |---*login_sta.py
    |---driver/
    |---package/
    |---run_bbs_test.py
    |---startup.bat
    |---自动化测试项目说明文档.docx
'''

'''
# mztestpro 

    # bbs：用于存放bbs项目的测试用例、测试报告、测试数据
    # driver/：用于存放浏览器驱动、selenium server服务，例如java -jar selenium-server-standalone-2.53.0.jar、chromedriver.exe、geckodriver.exe、IEDriverServer.exe等
    在执行测试用例前，将需要的浏览器驱动放到python path路径下，或者启动selenium server服务
    # package/：用于存放自动化所用到的扩展包，例如HTMLTestRunner.py 属于一个单独的模块，并且对其做了修改，所以在执行测试前需要将他复制到python下面的lib目录下。
    # run_bbs_test.py：运行文件，项目主程序，用于运行改BBS项目下的测试用例    
    # startup.bat： 用于启动selenium server服务 默认启动driver目录下的selenium-server-standalone-2.53.0.jar
    # 自动化测试项目说明文档.docx:介绍当前项目的架构，配置和说明文档    

'''

'''
# bbs
    data:存放测试相关的数据
    report：存放测试后的HTML报告，下面的image用于存放测试过程中的截图
    test_case：测试用例目录，用于存放测试用例及相关模块
'''

'''
# test_case：
    # models：该目录下存放一些公共的配置函数或者公共类。
    # page_obj.py：该目录用于存放测试用例的页面对象，page object，根据自定义规则，以*page.py命名的文件为封装的页面对象文件
    # *login_sta.py：测试用例文件，根据测试文件匹配规则，以*_sta.py命名的文件将被当做自动化测试用例执行
    
'''

