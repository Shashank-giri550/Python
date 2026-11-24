"""Problem Statement

An online examination records responses as c(correct),w(wrong),or(skipped).Award 4 marks for each correct answer, deduct 1 mark for each wrong answer, and award 0 for skipped answers.

Input:
5
C W C S C 

Output:
Score: 11
Correct: 3, Wrong: 1, Skipped: 1"""


n = int(input())
temp = input().split()
C = W = S = 0
for r in temp:
    if r == "C":
        C+=1
    elif r == "W":
        W+=1
    elif r == "S":
        S+=1
score = 4*C-W
print("Score:",score)
print(f"Correct: {C}, wrong: {W}, skipped: {S}")                