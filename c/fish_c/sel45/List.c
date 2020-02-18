/*************************************************************************
	> File Name: List.c
	> Author: wwh
	> Mail: 553954949@qq.com 
	> Created Time: Thu 12 Dec 2019 03:15:25 PM CST
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct Book
{
	char title[128];
	char author[40];
	struct Book *next;
};


void getInput(struct Book *book);
void addBookHead(struct Book **library);
void addBookTail(struct Book **library);
void printLibrary(struct Book *library);
void printBook(struct Book *book);
void releaseLibrary(struct Book **library);
struct Book *searchBook(struct Book *library,char *target);
void deletebook(struct Book **library,char *title);

void getInput(struct Book *book)
{
	printf("请输入书名：");
	scanf("%s",book->title);
	printf("请输入作者：");
	scanf("%s",book->author);
}

void releaseLibrary(struct Book **library)
{
	struct Book *temp;
	while(*library != NULL)
	{
		temp = *library;
		*library = (*library)->next;
		free(temp);
	}
}

void printLibrary(struct Book *library)
{
	struct Book *book;
	int count = 1;

	book = library;
	while(book != NULL)
	{
		printf("Book%d:\n",count++);
		printf("书名：%s\n",book->title);
		printf("作者：%s\n",book->author);
		book = book->next;
	}
}
 
void printBook(struct Book *book)
{
	printf("书名：%s\n",book->title);
	printf("作者：%s\n",book->author);
}
void addBookTail(struct Book **library)
{
	struct Book *book;
	static struct Book *tailPtr;
	book = (struct Book *)malloc(sizeof(struct Book));

	if(book == NULL)
	{
		printf("内存分配失败！\n");
		exit(1);
	}
	getInput(book);

	if(*library != NULL)
	{
		tailPtr->next = book;
		book->next = NULL;
	}
	else
	{
		*library = book;
		book->next = NULL;
	}
	tailPtr = book;
	//free(book);
}

void addBookHead(struct Book **library)
{
	struct Book *book,*temp;

	book = (struct Book *)malloc(sizeof(struct Book));
	if (book == NULL)
	{
		printf("内存分配失败！\n");
		exit(1);
	}
	getInput(book);

	if(*library != NULL)
	{
		temp = *library;
		*library = book;
		book->next = temp;
	}
	else
	{
		*library = book;
		book->next = NULL;
	}


	//free(book);
}


struct Book *searchBook(struct Book *library,char *target)
{
	struct Book *book;

	book = library;
	while(book != NULL)
	{
		if(strcmp(book->title,target) || strcmp(book->author,target))
		{
			break;
		}
		book = book->next;
	}
	return book;
}
void deletebook(struct Book **library,char *title)
{
	struct Book *book_cur,*book_pre;

	book_cur = *library;
	book_pre = NULL;
	while(book_cur != NULL && !(strcmp(book_cur->title,title)))
	{
		book_pre = book_cur;
		book_cur = book_cur->next;
	}
	if (book_cur == NULL)
	{
		printf("找不到！\n");
		return ;
	}
	else
	{
		if(book_pre == NULL)
		{
			*library = book_cur->next;
		}
		else
		{
			book_pre->next = book_cur->next;
		}
		free(book_cur);
	}
}
int main(void)
{
	struct Book *library = NULL; //head
	int ch;
	char input[128];
	while(1)
	{
		printf("请问是否需要录入书籍信息（y/n）：");
		do
		{
			ch = getchar();
		}while(ch != 'y' && ch != 'n');

		if (ch == 'y')
		{
			addBookTail(&library);
		}
		else
		{
			break;
		}
	}
	printf("请问是否需要输出书籍信息（y/n）：");
	do
	{
		ch = getchar();
	}while(ch != 'y' && ch != 'n');

	if (ch == 'y')
	{
		printLibrary(library);
	}

	printf("请输入书名或作者：");
	scanf("%s",input);
    
	struct Book *book;
	book = searchBook(library,input);
	if(book == NULL)
	{
		printf("很抱歉，没有找到！\n");
	}
	else
	{
		do
		{
			printf("已找到符合条件的图书...\n");
			printBook(book);
		}while( (book = searchBook(book->next,input)) != NULL);
	}

	printf("请输入想删除的书名：");
	scanf("%s",input);
	deletebook(&library,input);

	printf("请问是否需要输出书籍信息（y/n）：");
	do
	{
		ch = getchar();
	}while(ch != 'y' && ch != 'n');
	printLibrary(library);
	releaseLibrary(&library);
	return 0;
}
