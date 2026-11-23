"""Problem statement
A vending machine receives the item price and amount paid. Calculate the change and display the minimum number of currency notes and coins using denominations rupees 500,200,100,50,20,105,1 Greedy denomination selection is used to obtain the minimum number of notes and coins.

Input:
135 500

Output:
Change: Rs. 0
500: 0, 200: 0, 100: 1, 50: 1, 20: 0, 10: 1, 5: 1, 1: 0
"""

price,paid = map(int,input().split())

amount = paid - price
print("Change: Rs.",amount)

notes = [500, 200, 100, 50, 20, 10, 5, 1]
result = []

for note in notes:
    count = amount//note
    amount = amount%note
    result.append(f"{note}: {count}")
print(", ".join(result))    