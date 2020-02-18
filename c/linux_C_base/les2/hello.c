#include<stdio.h>
#include"max.h"
#include"min.h" 

int main()
{
    int a1=33;
    int a2=22;
    int maxNum=max(a1,a2);
    int minNum=min(a1,a2);
    printf("max:%d,min:%d\n",maxNum,minNum);
    return 0;
}
