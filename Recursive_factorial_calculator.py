"""Problem Statement

The factorial of a non-negative integer is the product of all positive integers less than or equal to that number.

Write a python program using a recursive function named factorial () to calculate the factorial of a given number.

Input:
0

Output:
1"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)
n = int(input())
print(factorial(n))  
    