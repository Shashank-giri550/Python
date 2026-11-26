"""A sorted list contains integers in ascending order. Given a target value, use searching to find its position. if the target is not present,display0.

Input:
6 7
1 3 5 7 9 11

Output:
Position: 4
"""

n,target = map(int,input().split())
arr = list(map(int,input().split()))

pos = 0
for i in range(n):
    if arr[i]== target:
        pos=i+1
        break
print("Position:",pos)    