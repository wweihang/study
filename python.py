# -*- coding: utf-8 -*-
import os 


# 遍历文件夹下所有文件
path = "F:/new" #文件夹目录 
datas = [] 

def eachFile(filepath): 
	fileNames = os.listdir(filepath) # 获取当前路径下的文件名，返回List 
	for file in fileNames: 
		newDir = filepath + '/' + file # 将文件命加入到当前文件路径后面 
		# print(newDir) 
		# if os.path.isdir(newDir): # 如果是文件夹 
		if os.path.isfile(newDir): # 如果是文件 
			if os.path.splitext(newDir)[1] == ".txt": # 判断是否是txt 
				f = open(newDir) 
				str = "" 
				for line in f.readlines(): 
					str = str + line # 读文件 datas.append(str) 
		else: 
			eachFile(newDir) #如果不是文件，递归这个文件夹的路径 

if __name__ == "__main__": 
	eachFile(path) 
	print(datas)



随机整数：
>>> import random
>>> random.randint(0,99)
21

随机选取0到100间的偶数：
>>> import random
>>> random.randrange(0, 101, 2)
42

随机浮点数：
>>> import random
>>> random.random() 
0.85415370477785668
>>> random.uniform(1, 10)
5.4221167969800881

随机字符：
>>> import random
>>> random.choice('abcdefg&#%^*f')
'd'

多个字符中选取特定数量的字符：
>>> import random
random.sample('abcdefghij',3) 
['a', 'd', 'b']

多个字符中选取特定数量的字符组成新字符串：
>>> import random
>>> import string
>>> string.join(random.sample(['a','b','c','d','e','f','g','h','i','j'], 3)).r
eplace(" ","")
'fih'

随机选取字符串：
>>> import random
>>> random.choice ( ['apple', 'pear', 'peach', 'orange', 'lemon'] )
'lemon'

洗牌：
>>> import random
>>> items = [1, 2, 3, 4, 5, 6]
>>> random.shuffle(items)
>>> items
[3, 2, 5, 6, 4, 1]




def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        　# 创建目录操作函数
        os.makedirs(path) 
        print path+' creat'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path+' exists'
        return False
# 定义要创建的目录
mkpath="d:\\qttc\\web\\"
# 调用函数
mkdir(mkpath)


    import os
     
    if os.path.exists(path):
        os.remove(path)


def draw_plt(predit,label):
    names = range(predit.shape[0])
    names = [str(x) for x in list(names)]
    x = range(len(names))
    plt.plot(x, predit, marker='.', mec='r',label='predit')
    plt.plot(x, label, marker='.', ms=2,label='label')
    plt.legend()
    plt.xticks(x, names, rotation=1)
    plt.margins(0)
    plt.subplots_adjust(bottom=0.10)
    plt.xlabel('time') 
    plt.ylabel("value") 
    pyplot.yticks([0.750,0.800,0.850])
    plt.show()
    plt.title("A simple plot") 

def plot_spectrogram(spec, note):
    fig = plt.figure(figsize=(20, 5))
    heatmap = plt.pcolor(spec)
    fig.colorbar(mappable=heatmap)
    plt.xlabel('Time(s)')
    plt.ylabel(note)
    plt.tight_layout()
    plt.show()



#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import time
# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 


#并行
import multiprocessing as mp
def printf_name(strin):
    print strin
dataset = ['BirdVox-DCASE-20k', 'ff1010bird', 'warblrb10k', 'PolandNFC', 'warblrb10k-eval']
pool = mp.Pool(mp.cpu_count())
results = pool.map(printf_name, [row for row in dataset])
pool.close()



#读取文件夹里的文件

