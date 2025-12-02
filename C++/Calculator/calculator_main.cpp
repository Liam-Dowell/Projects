#include <iostream>
#include <iomanip>
#include <cmath>
#include <string>
#include <limits>
using namespace std;

int addition_main();
int subtraction_main();
int multiplication_main();
int division_main();

int calculator_main()
{
    #define variable
    int choice;

    cout << "Welcome to Nasty Spider's Calculator.\n";
    cout << "What would you like to do?\n";
    cout << "1) Addition\n";
    cout << "2) Subtraction\n";
    cout << "3) Muliplication\n";
    cout << "4) Division\n";
    cin >> choice;

    if (choice == 1)
    {
        addition_main();
        calculator_main();
    }
    else if (choice == 2)
    {
        subtraction_main();
        calculator_main();
    }
    else if (choice == 3)
    {
        multiplication_main();
        calculator_main();
    }
    else if (choice == 4)
    {
        division_main();
        calculator_main();
    }
    else
    {
        cout << "Invalid choice. Please select a valid option.\n";
    }
    return 0;
}