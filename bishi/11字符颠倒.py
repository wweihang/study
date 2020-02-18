# coding:UTF-8
#字符颠倒
import sys
#while True:
#    try:
#        print sys.stdin.readline().strip("\n").[::-1]
#    except:
#        break


#句子颠倒

while True:
    try:
        line = sys.stdin.readline().strip("\n").split(" ")[::-1]
        print ' '.join(line)
    except:
        break
