# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/7/13 8:49
# @Software       : Python_study
# @Python_verison : 3.7

# 1、管道 |
'''
Linux管道主要是用来临时存储的，存在于两个命令之间,前一个命令的输出作为后一个命令的输入
[kduser@v-meter-sphere ~]$ echo 'hello linux'| grep hello

'''

# 2、正则表达式
'''
正则表达式是一种匹配数据的方法
1、普通正则：
    .:      匹配除了换行符以外的任意字符
    \s:     匹配空白符
    \b:     匹配单词的开始或者结尾，汉堡包，\bjianghu\b
    [0 - 9] 或者\d：   匹配数字
    [a - z]，[A-Z]：  匹配字母
    *：      匹配前面的字符0次或者任意次
    ^:      匹配字符串的开始 ^j
    $:      匹配字符串的结尾 j$

2、扩展正则：
    常用的限定符：
        +：      重复一次或更多次
        ?：      重复零次或一次
        {n}：    重复n次
        {n,}：   重复n次或更多次
        {n,m}：  重复n到m次 | 表示或
    使用了扩展正则的话需要使用-E 参数
'''
# 3、三剑客
# 三剑客的功能非常强大，但我们只需要掌握他们分别擅长的领域即可：grep擅长查找功能，sed擅长取行和替换。awk擅长取列
# 三剑客都是一行一行处理，操作时，不会修改到源文件，只是输出到操作时候的屏幕上

# grep
'''
    命令格式 :grep [OPTIONS] PATTERN[FILE...]
    常用的可选的选项为:
        -v显示不被pattern匹配的行
        -n 显示被pattern匹配的行号
    grep 选项 正则表达式 文件
    grep -n root test.txt       显示包含root的行号
    grep -vn root test.txt      显示不包含root的行号

    grep ^s test.txt            显示以s开头的行
    grep u$ test.txt            显示以u结尾的行
    grep -r .sh$ ./             显示当前路径下的以.sh结尾的文件
'''



# sed
'''
    # sed是一种流编辑器，它一次处理一行内容。处理时，把当前处理的行存储在临时缓冲区中，称为“模式空间”（pattern space），
    # 接着用sed命令处理缓冲区中的内容，处理完成后，把缓冲区的内容送往屏幕。然后读入下行，执行下一个循环。
    命令格式：sed[-hn..][-e<script>][-f<script FILE>][FILE]
    -h：表示显示帮助
    -n：表示静默模式，仅显示script处理后的结果
    -e<script>：以选项中指定的script来处理输入输出的文本文件
    -f<script>：以选项中指定的script文件来处理输入输出的文本文件
    
    a：新增 sed -e '4 a newline' test.txt   在4行后插入
    c: 取代 sed -e '2,5 c jiangxi' test.txt   2 到第5行的整个数据使用jiangxi替代
    d: 删除 sed -e '2,5 d' test.txt           删除第2到第5行
    i：插入 sed -e '3 i yixiu' test.txt       在第3行前插入一行为yixiu
    p: 打印 sed -n /root/p test.txt           打印有root的行数据
    s: 取代 sed -e 's/root/jianghu/g' test.txt     用jianghu替代root，g表示会替换所有的root，如果不加g则只替换匹配的每一行的第一个root
'''


# awk
'''
    
'''