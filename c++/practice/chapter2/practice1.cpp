#include<iostream>
using namespace std;

/*practice 1*/
void p2_1(void)
{
	cout << "weihang wei!" << endl;
	cout << "Guandong Province,Shenzheng,China!" << endl;

	return;
}

/*practice 2*/
void p2_2(void)
{
	int i_long = 0;
        int i_out = 0;
	cout << "Input the distance in long,Please!" << endl;	
	cin >> i_long;
	i_out = i_long * 220;
	cout << "the distance in filed:" << i_out << endl;
	
	return;  
}

/* practice 3*/
void str1(void)
{
	cout << "Three blind mice" << endl;
}

void str2(void)
{
	cout << "See how they run" << endl;
}

/* practice 4*/

void p2_4(void)
{
	int i_age = 0;
	int i_month = 0;
	cout << "Enter your age:";
	cin >> i_age;
	cout << i_age << endl;
	i_month = i_age * 12;
	cout << i_age << " years contain " << i_month << " monthes!" << endl;

	return;
}


int main(int argc,char **argv)
{
	p2_4();
}
