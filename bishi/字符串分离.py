# coding:UTF-8
#题目描述
#•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
#•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
#输入描述:
#连续输入字符串(输入2次,每个字符串长度小于100)

#输出描述:
#输出到长度为8的新字符串数组

#示例1
#输入
#abc
#123456789
#输出
#abc00000
#12345678
#90000000

import sys
char1 = sys.stdin.readline().strip("\n")
char2 = sys.stdin.readline().strip("\n")

def printEight(str):
    n = len(str)%8
    if n != 8:
        for num_0 in range(8-n):
            str = str + '0'
    for i in range(len(str)/8):
        print str[i*8:(i+1)*8]

printEight(char1)
printEight(char2)
