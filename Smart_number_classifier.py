"""Problem statement

A security system classifies a number as spevial if it is divisble by 3 or 5,but not by both.count the special numbers and find the largest special number.

Input:
6
3 5 10 12 14 25

Output:
Special Numbers: 5
Largest special: 25"""

n = int(input())
nums = list(map(int,input().split()))

count = 0
largest = 0
for x in nums:
    if (x%3 == 0)!=(x%5 == 0):
        count+=1
        if x > largest:
            largest = x
print("Special Numbers:",count) 
print("Largest Special:",largest)           
