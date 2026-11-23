"""Problem statement:
An elevator has a maximum load capacity.Classify its status as normal (load upto 80%).Caution (Above 80% but with capacity ). or overloaded (above capacity).

TEST CASE-1

Input:
1000 500

Output:
Load: 50.00%
status: Normal

TEST CASE-2

Input:
1000 850
Output:
Load: 85.00%
Status: Caution

TEST CASE-3

Input:
500 600
Load: 120.00%
Status: Overloaded
"""

capacity,load = map(int,input().split())

percent = (load*100)/capacity
if percent <= 80:
    print("Load:", f"{percent:.2f}%")
    print("Status: Normal")
elif percent <= 100:
    print("Load:",f"{percent:.2f}%")
    print("Status: Caution")        
else:
    print("Load:",f"{percent:.2f}%")
    print("Status: Overloaded")
            