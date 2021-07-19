# Basic-Federal-Tax-Calculator
This is a basic federal tax calculator where one can input their gross taxable income after deductions and get the amount of annual tax they will pay.
## Objectives:
### To demonstrate use of Python's builtin dataclasses module.
The script uses Classes with a dataclass decorator.  This implementation is meant to show how one can use Pythons built in dataclasses module available beginning with Python 3.7.
### To demonstrate test driven development using Python's builtin unittest module.
Specifically, the test script demonstrates how one can test Python classes. In this case the method of the class returns a string which is tested using unittest assertion type "assertEqual()" method.
In order to utilize the test script open a terminal and nevigate to the directory where the test script and the script being tested are located.
enter the following:
python -m unittest test_fed_tax_calculator.py
If everything tests Okay you will see the following:
