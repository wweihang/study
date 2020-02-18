# coding:UTF-8
#题目描述
#写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。

#输入描述:
#第一行输入一个有字母和数字以及空格组成的字符串，第二行输入一个字符。

#输出描述:
#输出输入字符串中含有该字符的个数。

#示例1
#输入
#ABCDEF
#A
#输出
#1

import sys
#while True:
#    try:
#        str = sys.stdin.readline().strip("\n").lower()
#        char = sys.stdin.readline().strip("\n").lower()
#        print str.count(char)
#    except:
#        break


#题目描述
#编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)，换行表示结束符，不算在字符里。不在范围内的不作统计。

#输入描述:
#输入N个字符，字符在ACSII码范围内。

#输出描述:
#输出范围在(0~127)字符的个数。

#示例1
#输入
#abc
#输出
#3


while True:
    try:
        str_ = sys.stdin.readline().strip("\n")
        print len(str_)
    except:
        break
