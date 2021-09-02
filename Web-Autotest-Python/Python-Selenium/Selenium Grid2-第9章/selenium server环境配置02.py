# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/5/24 8:37
# @Software       : Python-Selenium
# @Python_verison : 3.7
# 1、下载selenium server
# 下载地址：http://selenium-release.storage.googleapis.com/index.html

# 2、下载jdk
# 下载地址：https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
# 下载Windows x64文件格式为exe的
# 3、安装jdk

# 4、配置环境变量
'''
(1)新建->变量名"JAVA_HOME"，变量值"C:\Java\jdk1.8.0_05"（即JDK的安装路径）-----> 注意结尾不要带；号
(2)编辑->变量名"Path"，在原变量值的最后面加上“;%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin”
(3)新建->变量名“CLASSPATH”,变量值“.;%JAVA_HOME%\lib;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar”
'''
# 5、确认环境配置是否真确：
# 在控制台分别输入java，javac，java -version 命令，出现如下所示的JDK的编译器信息，包括修改命令的语法和参数选项等信息。

# 6、运行selenium server，切换到selenium server所在的目录，执行 java -jar selenium-server-standalone-3.8.0.jar
# 提示:selenium server is up and runing

# 在selenium1.0的时候，我们执行selenium RC脚本时依靠的是 selenium server，在selenium2.0时，webdriver取代了selenium RC
# 提供了各种浏览器的驱动而不是使用内置浏览器去执行js脚本

