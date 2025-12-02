#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
using namespace std;

int division_main()
{
    double num1, num2, quotient;
    cout << "Welcome to the division function!\n";
    cout << "Enter the number you want to divide";
    cout << ":> ";
    cin >> num1;
    cout << "Enter the number you want to divide by";
    cout << ":> ";
    cin >> num2;

    if (num2 == 0)
    {
        cout << "Error: Division by zero is undefined.\n";
        return 1;
    }

    quotient = num1 / num2;
    cout << "The quotient of " << num1 << " divided by " << num2 << " is: " << quotient << endl;
    return 0;
}