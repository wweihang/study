# coding:UTF-8
#题目描述
#给定n个字符串，请对n个字符串按照字典序排列。
#输入描述:
#输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
#输出描述:
#数据输出n行，输出结果为按照字典序排列的字符串。
#示例1
#输入
#9
#cap
#to
#cat
#card
#two
#too
#up
#boat
#boot
#输出
#boat
#boot
#cap
#card
#cat
#to
#too
#two
#up
import sys
#while True:
#    try:
#        num = int(sys.stdin.readline().strip("\n"))
#        ret = []
#        for i in range(num):
#            ret.append(sys.stdin.readline().strip())
#        for str_ in sorted(ret):
#            print str_
#    except:
#        break

#题目描述
#输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。

#输入描述:
# 输入一个整数（int类型）
#输出描述:
# 这个数转换成2进制后，输出1的个数

#示例1
#输入
#5
#输出
#2
#while True:
#    try:
#        input_ = int(sys.stdin.readline().strip())
#        cout = 0
#        while input_ > 1:
#            input_ = input_ / 2
#            cout += 1
#        print cout
#    except:
#        break

#题目描述
#开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
#输入：
#合法坐标为A(或者D或者W或者S) + 数字（两位以内）
#坐标之间以;分隔。
#非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。
#下面是一个简单的例子 如：
#A10;S20;W10;D30;X;A1A;B10A11;;A10;
#处理过程：
#起点（0,0）
#+   A10   =  （-10,0）
#+   S20   =  (-10,-20)
#+   W10  =  (-10,-10)
#+   D30  =  (20,-10)
#+   x    =  无效
#+   A1A   =  无效
#+   B10A11   =  无效
#+  一个空 不影响
#+   A10  =  (10,-10)
#结果 （10， -10）
#输入描述:
#一行字符串
#输出描述:
#最终坐标，以,分隔
#示例1
#输入
#A10;S20;W10;D30;X;A1A;B10A11;;A10;
#输出
#10,-10
import sys
while True:
    try:
        input_ = raw_input().strip().split(";")
        x,y = 0,0
        for i in input_:
            if len(i) < 3:
                continue
            if i[0] == "A":
                try:
                    tmp = int(i[1:])
                except:
                    continue
                x -= tmp
            elif i[0] == "S":
                try:
                    tmp = int(i[1:])
                except:
                    continue
                y -= tmp
            elif i[0] == "D":
                try:
                    tmp = int(i[1:])
                except:
                    continue
                x += tmp
            elif i[0] == "W":
                try:
                    tmp = int(i[1:])
                except:
                    continue
                y += tmp
        print '%d,%d'%(x,y)
    except:
        break
