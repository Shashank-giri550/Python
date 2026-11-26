"""Problem Statement

A sports receives 3 points for every win. 1 points for every draw,and0points for every loss.Calculate its total points,number of matches played,and win percentage.

Input:
1 2 1

Output:
Matches: 4
Points: 5
Win Rate: 25.00%
"""

wins,draw,losses = map(int,input().split())
match = wins+draw+losses
total = 0
for i in range(match):
   if i < wins:
     total+= 3
   elif i<wins+draw:
     total+= 1
   else:
     total+= 0
     
win_rate = (wins/match)*100     
print("Matches:",match)
print("Points:",total)    
print(f"Win Rate: {win_rate:.2f}%")             