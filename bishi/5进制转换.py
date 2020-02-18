# coding:UTF-8
#题目描述
#写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。（多组同时输入 ）

#输入描述:
#输入一个十六进制的数值字符串。

#输出描述:
#输出该数值的十进制字符串。

#示例1
#输入
#0xA
#输出
#10

import sys
while True:
    try:
        str = sys.stdin.readline().strip()
        tempstr = int(str[2:],base=16)
        print tempstr
    except:
        break
