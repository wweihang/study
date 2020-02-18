# coding:UTF-8

#功能:输入一个正整数，按照从小到大的顺序输出它的所有质数的因子（如180的质数因子为2 2 3 3 5 ）

#最后一个数后面也要有空格

#详细描述：


#函数接口说明：

#public String getResult(long ulDataInput)

#输入参数：

#long ulDataInput：输入的正整数

#返回值：

#String

import sys
#while True:
#    try:
#        num = int(sys.stdin.readline().strip())
#        i = 2
#        while num != 1:
#            if num % i == 0:
#                print i
#                num = num / i
#            else:
#                i += 1
#        print  " "
#    except:
#        break


#写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
while True:
    try:
        input_ = float(sys.stdin.readline().strip())
        if input_ - int(input_) >= 0.5:
            print int(input_)+1
        else:
            print int(input_)
    except:
        break
