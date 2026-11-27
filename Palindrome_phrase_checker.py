"""Problem Statement

A text application checks whether a phrase is a palindrome. A phrase is a palindrome.if it reads the same forward and backward after ignoring spaces.

Input:
madam

Output:
Palindrome: Yes
"""

x = input().strip()
y = x.lower()

if y == y[::-1]:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")    
    