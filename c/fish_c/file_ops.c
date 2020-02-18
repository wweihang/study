/*************************************************************************
	> File Name: file_ops.c
	> Author: wwh
	> Mail: 553954949@qq.com 
	> Created Time: Mon 16 Dec 2019 05:33:07 PM CST
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX 1024
/****58
//int main(void)
{
	FILE *fp1;
	//FILE *fp2;
	char ch[MAX];

	if((fp1 = fopen("hello.txt","w")) == NULL)
	{
		printf("文件读取失败！\n");
		exit(EXIT_FAILURE);
	}

	fputs("你叫什么名字？\n",fp1);
	fputs("你住哪里？\n",fp1);
	fputs("你的职业是什么？",fp1);
	fclose(fp1);

	if((fp1 = fopen("hello.txt","r")) == NULL)
	{
		printf("文件读取失败！\n");
		exit(EXIT_FAILURE);
	}

	while(!(feof(fp1)))
	{
		fgets(ch,MAX,fp1);
		printf("%s\n",ch);		
	}


	// if((fp2 = fopen("hello_cp.txt","w")) == NULL)
	// {
	// 	printf("文件读取失败！\n");
	// 	exit(EXIT_FAILURE);
	// }
	//fgetc fputc 读取或写入单个字符
\n// while((ch = fgetc(fp1)) != EOF)
\n// {
\n// 	fputc(ch,fp2);
\n// 	//putchar('\t');
\n// }
\n
\n
\n
\n
	fclose(fp1);
	//fclose(fp2);
	return 0;
}

*****/

#include <time.h>
 
int main(void)
{
	FILE *fp;
	struct tm *p;
	time_t t;
	
	time(&t);//获取时间值 
	p = localtime(&t);//转换
	
	if ((fp = fopen("date.txt", "w")) == NULL)//w:不存在创建,存在打开初始化 
	{
		printf("打开文件失败！\n");
		exit(EXIT_FAILURE);
	}
	
	fprintf(fp, "%d-%d-%d", 1900 + p->tm_year, 1 + p->tm_mon, p->tm_mday);
 
	fclose(fp);//写入完后要关闭，可以确保所有数据写到文件中 
	
	
	int year, month, day;
	
	if ((fp = fopen("date.txt", "r")) == NULL)//w:不存在创建,存在打开初始化 
	{
		printf("打开文件失败！\n");
		exit(EXIT_FAILURE);
	}
	
	fscanf(fp, "%d-%d-%d", &year, &month, &day);
	printf("%d-%d-%d\n", year, month, day);
	
	fclose(fp);
	
	return 0; 
}
