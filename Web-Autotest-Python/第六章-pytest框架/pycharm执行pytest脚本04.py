# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/5/1 10:19
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
# 之前执行python文件时候，我们在文件中直接右键，然后run
# 执行unittest脚本时候，我们是run unittest
# 但是执行pytest脚本时直接执行是不生效的，这个时候，需要我们设置一下编辑器pycharm的关于该文件的默认runner

# 配置路径：setting--->baidu_tools--->python integrated baidu_tools --->testing--->default tester runner
# 配置完成后需要在该文件的父目录下右键进行执行，在该文件上执行还是不行的

# pycharm运行脚本总结：
    # 分为Python文件和 Python test
    # 如果文件中有：if __name__ == '__mian__' 那么是按照Python的运行方式运行的
    # 如果没有我们可以去配置文件以哪种方式运行
    # pycharm解释器，会默认记忆我们上一次的运行方式。


