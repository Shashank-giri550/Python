"""Problem Statement

A company records daily expenses. Expenses at odd positions are added and expenses at even positions are subtracted,using 1-based positions. Calculate the final balance and classify it as positive,negative or zero.

Input:
5
100 50 200 100 300

Output:
Balance: 450
Status: Positive
"""

n = int(input())
exp = list(map(int, input().split()))

balance = 0
for i in range(n):
    if i % 2 == 0:      # 1-based odd position
        balance += exp[i]
    else:               # 1-based even position
        balance -= exp[i]

print("Balance:", balance)
if balance > 0:
    print("Status: Positive")
elif balance < 0:
    print("Status: Negative")
else:
    print("Status: Zero")