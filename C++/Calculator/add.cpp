#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
using namespace std;

int addition_main()
{
    int count;
    double num, sum;
    cout << "Welcome to the addition function!\n";
    cout << "How many numbers would you like to add? ";
    cout << ":> ";
    cin >> count;
    for (int i = 1; i <= count; i++)
    {
        cout << "Enter number " << i << ": ";
        cout << ":> ";
        cin >> num;
        sum += num;
    }
    cout << "The sum of those numbers are: " << sum << endl;
    return 0;

}
