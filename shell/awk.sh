#!bin/bash

#取文本第一行
awk 'NR==1{print}' file.txt

awk -v num=$i 'NR==num {print}' file.txt

#取文本第一列
cat addnoise.txt |awk '{print $1}' #  |sort | uniq

# 取文本若干列
cat addnoise.txt | awk '{for (i=2 ;i<=NF;i++) printf $i " "; printf "\n" }' 

#文本行数
num = `cat filelist | awk '{print NR}' |tail -n1`
num=`awk 'END{print NR}' lst1`
#数字去前面的0
file_num=`echo $file_num1 |sed 's/^0\+//'`


#match 包含
cat aishell_transcript_v0.8.txt |awk '{if (match($1,"S0712")) {printf ("%s\n",$0)}}'
cat aishell_transcript_v0.8.txt |awk awk -F "\t" '{if (match($1,"S0712")) {gsub($1,"H0001","S0712"); printf ("%s\n",$0)}}'

awk -F "\t" '{if(match($1,"S0712")) {gsub("","H0001");print $0}}'  aishell_transcript_v0.8.txt
#字符串比较
cat addnoise.txt |awk -v user=$file '{if ($1 == user){ print}}'
cat $text |awk -v name=$old_name_prefix -v replace=$new_name_prefix '{if($1==name) {{$1=""}{print replace$0}}}'


sed 's/ /\n/g ' txt |awk '{printf $NR}'


comm - 12     就只显示在两个文件中都存在的行；
comm - 23    只显示在第一个文件中出现而未在第二个文件中出现的行；
comm - 123  则什么也不显示。
例如：找出a.txt文件有而b.txt文件中没有的放在c.txt文件中

    #!/bin/sh  
    # author by tianmo  
    # date 2011-11-21 20:33  
    #BEGIN  
    cat a.txt | sort | uniq | sort > a_u.txt  
    cat b.txt | sort | uniq | sort > b_u.txt  
    comm -23  a_u.txt  b_u.txt > c.txt  
    # END  
