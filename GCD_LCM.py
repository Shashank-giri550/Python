""" Problem Statement

A mathematics application receives two positive integers. Calculate thier Greatest Common Divisor (GCD) and Least common multiple(LCM)

Input:
12 18

Output:
LCM: 36
GCD: 6
"""

a,b = map(int,input().split())

x = max(a,b)

while True:
    if x % a == 0 and x % b == 0:
        print("LCM:",x)
        break 
    x+=1
g = min(a,b)
while g>0:
    if a%g == 0 and b%g == 0:
        print("GCD:",g)
        break
    g-=1
        