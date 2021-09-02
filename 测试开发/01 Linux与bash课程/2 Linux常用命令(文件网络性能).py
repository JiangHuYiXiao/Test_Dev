# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/7/12 9:05
# @Software       : Python_study
# @Python_verison : 3.7

# ctrl +c退出命令

# 我们的Linux命令分为：
    # 1、文件相关的命令（cd\ls\pwd\touch\rm -rf\mkdir\rmdir\mv\cp\more\cat\gedit）两个特殊的文件相关的命令(重定向：>,管道：|)
        # rm -rf 文件名或者目录名
        # mv 源文件 替换后的文件路径 文件名或者目录名

        # 文件属性：
            # -rw-r--r-- 1 HSZC1712-0006+Administrator 197121 1102 七月 12 08:49 '1 Linux系统与shell命令.py'
            # -rw-r--r-- 1 HSZC1712-0006+Administrator 197121  527 七月 12 19:32 '2 Linux常用命令(文件网络性能).py'
            # 权限属性 连接数 所有者                       用户组 大小 修改日期        文件或目录名

            # -rw-r--r--    -：表示文件  rw-：表示所有者用友读写的权限  r--:表示所属组的权限只有读  r--:表示其他用户的权限只有读
        # 权限修改：
            # r：read 值为4，w：write 值为2，x：execute
            # chmod 777 test  第一个7表示所有者的权限（读写执行），第二个7表示所属组的权限（读写执行），第三个7表示其他用户权限（读写执行）

            # -rw-r--r-- 1 HSZC1712-0006+Administrator 197121    9 七月 12 19:56  test.txt
            # 修改权限 chmod 777 test.txt
            # 修改后：
            # -rwxrwxrwx 1 HSZC1712-0006+Administrator 197121    9 七月 12 19:56  test.txt
    # 2、网络相关的命令
    #     ping 测试网络连接情况
        # netstat 网络系统的状态信息
    # 3、性能相关的命令
    # top  持续监视系统性能，实时监控
    # ps  查看进程信息  -aux显示所有进程包括用户分组情况，只是一个时间点

