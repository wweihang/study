/*************************************************************************
	> File Name: enum_test.c
	> Author: wwh
	> Mail: 553954949@qq.com 
	> Created Time: Mon 16 Dec 2019 01:45:54 PM CST
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//位域是在结构体基础上变形而来的
//Test结构体总共占了4位 
struct Test
{
	unsigned int a:1;//占1个二进制位 
	//unsigned int b;//错误的，unsigned int，4位，32字节 
	unsigned int c:2;//占2个二进制位 
};

int main(void)
{
	// enum week{mon=1,tue,wed,thur,fri,sat,sun};
	// enum week today,temp;
	// //mon = 101;//错误，一确定下来，就是常量，无法修改 
	// printf("tue = %d\n", tue);
	// printf("thur = %d\n", thur);
	// printf("sat = %d\n", sat);

	// temp = 2.5;
	// printf("temp = %d\n", temp);
	// return 0;



 
	struct Test test;
	test.a = 0;
	//test.b = 1;
	test.c = 2;//十进制的2,二进制形式是10，所以要两个二进制位来存放
	
	printf("a = %d,c = %d\n", test.a, test.c);
	printf("size of test = %d\n", sizeof(test));
 
	return 0;

}