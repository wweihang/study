# coding:UTF-8
#题目描述
#数据表记录包含表索引和数值（int范围的整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

#输入描述:
#先输入键值对的个数
#然后输入成对的index和value值，以空格隔开

#输出描述:
#输出合并后的键值对（多行）

#示例1
#输入

#4
#0 1
#0 2
#1 2
#3 4
#输出
#0 3
#1 2
#3 4
import sys
while True:
    try:
        num = int(sys.stdin.readline().strip("\n"))
        d = {}
        for i in range(num):
            k,v = map(int,sys.stdin.readline().strip("\n").split(" "))
            d[k] = d.setdefault(k,0) + v
        for k in sorted(d.keys()):
            print k,d[k]
    except:
        break


#题目描述
#输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。

#输入描述:
#输入一个int型整数

#输出描述:
#按照从右向左的阅读顺序，返回一个不含重复数字的新的整数

#示例1
#输入
#9876673
#输出
#37689

while True:
    try:
        input_ = sys.stdin.readline().strip("\n")
        tmp = input_[::-1]
        ret = ""
        for i in tmp:
            if i not in ret:
                ret += i
        print ret
    except:
        break
