# -*- coding:utf-8 -*-
'''
1、二进制：
计算机能够识别的语言是机械语言，也就是我们所说的二进制:00011001 11110001

2、ASCII码：
之前说过python2 默认编码为Ascii，Ascii码中只包含英文字母、数字、特殊字符，不包含中文，所以用python2运行中文需要在文件头申明编码格式。
ASCII最多支持2**8个字符。一个英文字母为一个字节为8位，也就是8个二进制。 1byte == 8bit
所有ASCII码的最左边一个是0，因为刚开始设计为7位就满足了美国所有编码，为了后续扩展多留了一位，多的补充0.
1byte（字节）== 8bit
1KB ==1024byte
1MB  ==1024KB
1GB  ==1024M
1TB  ==1024G

3、Unicode
随着计算机的发展，到了中国需要支持中文以及其他国家语言，美国开发了一套新的编码表，我们称为Unicode，万国码。
作用：
支持全球所有国家的语言。
有一套完整的编码映射表。
Unicode中：
一个英文字母为2个字节表示，足够了 2**16 ==65536
一个中文用4个字节表示，足够了    2**32 == 4294967296
一个字符，不管是英文或者中文或者特殊字符，都是用两个字节，
后面因为中文用两个字节表示不了2**16==65536，所以升级到了32位，才可以满足所有国家的语言

4、UTF-8
虽然Unicode用4个字节表示中文足够了，但是却太浪费了，所以出现了对Unicode的升级为utf-8
在utf -8中:
一个中文为3个字节，(2**24)==16777216
一个英文为1个字节
欧洲用两个字节

5、GBK
我们自己国家开发的编码表，一个中文用两个字节，英文用一个字节，包含2**16 == 65536个编码
 默认的编码就是GBK

'''

print(2**16)