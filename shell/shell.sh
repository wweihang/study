#!bin/bash

sed -e '/abc/d'  a.txt   // 删除a.txt中含"abc"的行，但不改变a.txt文件本身，操作之后的结果在终端显示
# 将某个文件中的hello字符串替换为hi
sed -i "s/hello/hi/g" test.txt
#shell 去空格

# 替换字符串
sed -i "s/jack/tom/g" test.txt
# 删除含字符串"abc"或“efg"的行，将结果保存到a.log
sed '/abc/d;/efg/d' a.txt > a.log    


 
#删除双引号
cat aa.txt |sed 's/\"//g' 
#删除行首空格   
sed 's/^[ \t]*//g'
#删除行末空格
sed 's/[ \t]*$//g'
#删除所有的空格  
sed s/[[:space:]]//g

提取文本中的中文字符
cat transcript_cmds_66 | sed 's/[a-zA-Z0-9[:punct:]]//g' | grep -v '^$' >1
sed s/[[:space:]]//g 1 >2   
#加序号  去空行
cat 2 |awk '{if($0 !=""){print NR“ ”$0;}}' >3 

# 按列合并文本
paste -d " " file1 file2 
# for循环
for((i=1; i<=98; i++))
do
{
}
done

for((i=1; i<=98; i++))
do
{
}&
done
wait

A="china fengxi zhongguo"
echo "echo varialbe A directly:" $A
echo ""
echo "loop string"
for i in $A;
do
    echo $i
done
 
 
A=("china" "fengxi" "zhongguo")
echo "echo array directly:" $A
echo ""
echo "loop array"
for i in ${A[@]};
do
    echo $i
done

数组的申明方式
array=(element1 element2 element3 .... elementN) 

数据读取
#echo ${array[0]}  
#echo ${array[index]} 
数据遍历
for data in ${array[@]}  
do  
    echo ${data}  
done 

#map
declare -A map=()
map[`cat $text1 |awk -v num=$i 'NR==num {print $1}'`]=`cat $text2 |awk -v num=$i 'NR==num {print $1}'`
new_name_prefix=`echo ${map[$name_prefix1]}`

#cut
name_prefix=`echo $f | cut -d "/" -f 3`

#字符串替换
要求： 将 "a/b/c" 转成 "a_b_c"
解法：
     str="a/b/c"
      echo ${str//\//_}


# 各种运算
#求余
a=1000
b=$(( $a % 5 ))
if [ $b = 0 ] ; then 
       echo "execute it"
else
       echo "Not execute"
fi
#取字符串的第19个字符之后的4个字符
file_num1=`echo ${file:19:4}`

#取字符串的zui后的5个字符
a1=`echo ${file:0-5}`

#加法
let file_num=file_num+3000

#取2位的整数位
a1=`printf "%.2d" $file_name`

#if(整数比较)
if [[ "$file_name" -le "9" ]];then

elif [[ "$file_name" -ge "10"  && "$file_name" -le "99" ]];then

else

fi


#find
find ./ -name file*


# 遍历文件夹下所有文件
function getdir(){
    for element in `ls $1`
    do  
        dir_or_file=$1"/"$element
        if [ -d $dir_or_file ]
        then 
            getdir $dir_or_file
        else
            echo $dir_or_file

        fi  
    done
}
root_dir="/home/weihang/data/小dot"

#shell 遍历数组
array=( A B C D 1 2 3 4)
for element in ${array[@]}
do
   echo $element
done

# 号截取，删除左边字符，保留右边字符。
var=http://www.aaa.com/123.htm
echo ${var#*//}
# 其中 var 是变量名，# 号是运算符，*// 表示从左边开始删除第一个 // 号及左边的所有字符
# 即删除 http://      结果是 ：www.aaa.com/123.htm

2. ## 号截取，删除左边字符，保留右边字符。
echo ${var##*/}
##*/ 表示从左边开始删除最后（最右边）一个 / 号及左边的所有字符   即删除 http://www.aaa.com/    结果是 123.htm

3. %号截取，删除右边字符，保留左边字符
echo ${var%/*}
#  %/* 表示从右边开始，删除第一个 / 号及右边的字符    结果是：http://www.aaa.com

4. %% 号截取，删除右边字符，保留左边字符
echo ${var%%/*}
 %%/* 表示从右边开始，删除最后（最左边）一个 / 号及右边的字符
结果是：http:

5. 从左边第几个字符开始，及字符的个数
echo ${var:0:5}
其中的 0 表示左边第一个字符开始，5 表示字符的总个数。
结果是：http:

6. 从左边第几个字符开始，一直到结束。

1
echo ${var:7}
 

其中的 7 表示左边第8个字符开始，一直到结束。
结果是 ：www.aaa.com/123.htm

7. 从右边第几个字符开始，及字符的个数

1
echo ${var:0-7:3}
 

其中的 0-7 表示右边算起第七个字符开始，3 表示字符的个数。
结果是：123

8. 从右边第几个字符开始，一直到结束。

1
echo ${var:0-7}
 

表示从右边第七个字符开始，一直到结束。
结果是：123.htm

注：（左边的第一个字符是用 0 表示，右边的第一个字符用 0-1 表示）
#判断文件后缀
if [ "${element2##*.}"x = "wav"x ];then
    cp $file/$element1/$element2/$element3 meeting_2/$element3
fi
