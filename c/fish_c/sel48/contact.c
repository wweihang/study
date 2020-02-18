/*************************************************************************
	> File Name: contact.c
	> Author: wwh
	> Mail: 553954949@qq.com 
	> Created Time: Thu 14 Dec 2019 03:15:25 PM CST
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX 1024 //定义内存池的空间1024 

typedef struct Person
{
	char name[20];
	char phone[40];
	struct Person *next;
}PERSON,*PPERSON;

//定义内存池为全局变量
//在调用 addPerson时，在内存池中检查，是否有废弃的空间直接可以拿来使用
//在调用 delPerson时，删除联系人时，把联系人放到内存池里面，检查内存池的空间是否合适 
PERSON *pool = NULL;//内齿池的单链表 
int count;//统计里面有多少块垃圾

void getInput(PERSON *person);                      //1、获取联系人信息
void displayContacts(PERSON *contacts);             //2、显示通讯录所有联系人信息
void printPerson(PERSON *person);                   //3、显示联系人信息
void addPerson(PERSON **contacts);                  //4、增加联系人（尾插入）
PERSON *findPerson(PERSON *contacts);        //5、查找联系人
void changePerson(PERSON *contacts);                //6、修改联系人
void delPerson(PERSON **contacts);                  //7、删除联系人
void releaseContacts(PERSON **contacts);            //8、释放通讯录
void releasePool(void);                                    //9、释放内存池 

//1、获取联系人信息
void getInput(PERSON *person)
{
    printf("请输入联系人姓名：");
    scanf("%s",person->name);
    printf("请输入联系人手机号码：");
    scanf("%s",person->phone);
}

//2、显示通讯录所有联系人信息
void displayContacts(PERSON *contacts)
{
    int count = 1;
    PERSON *temp;

    temp = contacts;
    while(temp != NULL)
    {
       printf("联系人%d：\n",count);
       printf("联系人姓名：%s\n",temp->name); 
       printf("联系人手机：%s\n",temp->phone);
       count += 1;
       temp = temp->next; 
    }
}

//3、显示联系人信息
void printPerson(PERSON *person)
{
    printf("联系人姓名：%s\n",person->name); 
    printf("联系人手机：%s\n",person->phone);
}

//4、增加联系人（尾插入）
void addPerson(PERSON **contacts)
{
    PERSON *temp;
    static PERSON *tail;
    
	//如果内存池非空，则直接从里面获取空间
	if (pool != NULL)//非空表示内存池有垃圾的空间，从头部取出来，给Person用 
	{
		temp = pool;
		pool = pool->next;
		count--;//内存池少了一块垃圾内存 
	} 
	//如果内存池为空，则调用mallc函数申请新的内存空间 
	else
	{
		temp = (PPERSON)malloc(sizeof(PERSON));
		if (temp == NULL)
		{
			printf("内存分配失败！\n");
			exit(1);
		}
	}
    getInput(temp);

    if(*contacts != NULL)
    {
        tail->next = temp;
        temp->next = NULL;
    }
    else
    {
        *contacts = temp;
        temp->next = NULL;
    }
    tail = temp;
}

//5、查找联系人
PERSON *findPerson(PERSON *contacts)
{
    PERSON *temp;
    char input[40];

    printf("请输入查找的联系人姓名：");
    scanf("%s",input);

    temp = contacts;
    while((temp != NULL) && strcmp(temp->name,input))
    {
        temp = temp->next;
    }
    return temp;
}


//6、修改联系人
void changePerson(PERSON *contacts)
{
    PERSON *person;
    person = findPerson(contacts);
    char ch;

    if(person == NULL)
    {
        printf("没有找到该联系人！\n");
    }
    else
    {
        printf("是否修改联系人姓名(y/n)?");
	    do
	    {
		    ch = getchar();
	    }while(ch != 'y' && ch != 'n');
        if(ch == 'y')
        {
            printf("新联系人的姓名：");
            scanf("%s",person->name);
        }
        printf("是否修改联系人手机(y/n)?");
	    do
	    {
		    ch = getchar();
	    }while(ch != 'y' && ch != 'n');
        if(ch == 'y')
        {
            printf("新联系人的手机：");
            scanf("%s",person->phone);
        }
    }
    
}

//7、删除联系人
void delPerson(PERSON **contacts)
{
    PERSON *person_cur,*person_pre,*temp;
    char input[40];

    printf("请输入删除的联系人姓名：");
    scanf("%s",input);

    person_cur = *contacts;
    person_pre = NULL;
    //定位到待删除的节点
    while((person_cur != NULL) && strcmp(person_cur->name,input))
    {
        person_pre = person_cur;
        person_cur = person_cur->next;
    }
    if(person_cur == NULL)
    {
        printf("没有找到该联系人！\n");
    }
    else
    {
        //待删除的节点是第一个节点
        if(person_pre == NULL)
        {
            *contacts = (*contacts)->next;
        }
        else
        {
            person_pre->next = person_cur->next;
        }
        //free(person_cur);

        if (count < MAX)
        {
            //头插法
            if(pool != NULL)
            {
                //把新的节点插入到链表的头部 
                temp = pool;  //保存原来head指针指向的地址 
                pool = person_cur; // head指针指向新的地址
                person_cur->next = temp; //把新节点的指针域指向原来head指针指向的地址
            } 
            else
            {
                pool = person_cur;
                person_cur->next = NULL;
            }    
        }
        else//没有空位
        {
            free(person_cur);
        }
        
    }  
}

//8、释放通讯录
void releaseContacts(PERSON **contacts)
{
    PERSON *temp;

    while(*contacts != NULL)
    {
        temp = *contacts;
        *contacts = (*contacts)->next;
        free(temp);
    }
}

//释放内存池 
void releasePool(void)
{
	PERSON *temp;
	
	while (pool != NULL)
	{
		temp = pool;
		pool = pool->next;
		free(temp);
	}
}

int main(void)
{
	int code;
	PERSON *contacts = NULL;
	PERSON *person;
	
	printf("| 欢迎使用通讯录管理程序 |\n");
	printf("|--- 1:插入新的联系人 ---|\n");
	printf("|--- 2:查找新的联系人 ---|\n");
	printf("|--- 3:更改新的联系人 ---|\n");
	printf("|--- 4:删除新的联系人 ---|\n");
	printf("|--- 5:显示新的联系人 ---|\n");
	printf("|--- 6:退出通讯录程序 ---|\n");
	while (1)
	{
		printf("\n请输入指令代码：");
		scanf("%d", &code);
		switch (code)
		{
			case 1: addPerson(&contacts); break;
			
			case 2: person = findPerson(contacts);
					if (person == NULL)
					{
						printf("找不到该联系人！\n");
					}
					else
					{
						printPerson(person);
					}
					break;
			
			case 3: changePerson(contacts); break;
			
			case 4: delPerson(&contacts); break;
			
			case 5: displayContacts(contacts); break;
			
			case 6: goto END;
		}
	}
 
END:
	releaseContacts(&contacts);
	releasePool();
	return 0;
}