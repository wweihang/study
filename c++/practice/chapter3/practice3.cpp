#include<iostream>
using namespace std;

/* practice 1*/
const int foot2inch = 12;
void p3_1(void)
{
	int i_inch = 0;
	int i_feet = 0;
	int i_inch_mod = 0;
	cout << "Please input your height in inch:___\b\b\b";
	cin >> i_inch;
	i_feet = i_inch / foot2inch;
	i_inch_mod = i_inch % foot2inch;

	cout << "your height in inch:" << i_inch << " your height in foot and inches:" << "(" << i_feet << "," << i_inch_mod << ")" << endl;
	
	return; 
}


/* practice 2*/
void p3_2(void)
{
	double d_inch = 0.0;
	double d_feet = 0.0;
	double d_meter = 0.0;
	double d_bound = 0.0;
	double d_kg = 0.0;
	double d_bim = 0.0;

	cout << "enter the height in inch and feet!" << endl;
	cout << "enter feet:";
	cin >> d_feet;
	//cout << d_feet <<endl;
	cout << "enter inches:";
	cin >> d_inch;
	//cout << d_inch << endl;

	cout << "enter the weight in bound:";
	cin >> d_bound;
	//cout << d_bound << endl;

	d_meter = (d_feet * 12 + d_inch) * 0.0254;
	d_kg = d_bound / 2.2;
	d_bim = d_kg / d_meter;
	cout << "the BMI:" << d_bim <<endl;
}

/* practice 3*/

void p3_3(void)
{
	double d_degree_in = 0.0;
	double d_minutes = 0.0;
	double d_seconds = 0.0;
	double d_degree_out = 0.0;

	cout << "Enter a latitude in degrees, minutes, and seconds:" << endl;
	cout << "First, enter the degrees:";
	cin >> d_degree_in;
	cout << "Next, enter the seconds of arc:";
	cin >> d_minutes;
	cout << "Finally, enter the seconds of arc:";
	cin >> d_seconds;
	d_degree_out = d_degree_in + d_minutes / 60 + d_seconds / 3600;
	cout << d_degree_in << " degrees, " << d_minutes << " minutes, " << d_seconds << " seconds = " << d_degree_out << " degrees" << endl;
}

int main(int argc,char **argv)
{
		
	p3_3();
}
