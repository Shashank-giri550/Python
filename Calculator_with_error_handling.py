"""Problem Statement

Read two numbers and an operator(+,-,*,/) and print the result. The program must not crash on division by zero,an invalid operator or an invalid number; it should print an error message instead (use try/except).

Input:
5
10 + 5
8 / 0
7 % 2
abc * 3
9 / 4

Output:
Result: 15.0
Error: Cannot divide by zero
Error: Unknown operator
Error: could not convert string to float: 'abc'
Result: 2.25
"""

def calculate(a,op,b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == a * b:
        return a * b
    if op == "/":
        return a / b
    raise ValueError("Unknown operator")
for i in range(int(input())):
    try:
        a, op, b = input().split()
        print("Result:",calculate(float(a),op,float(b)))
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except ValueError as e:
        print("Error:",e)        