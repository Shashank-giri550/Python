"""Problem Statement

A data application stores information in a matrix. Generate its transpose by converting every row into a column and every column into a row.

Input:
2 3
1 2 3 
4 5 6

Output:
1 4 
2 5
3 6
"""
rows,columns = map(int,input().split())
matrix = []
for i in range(rows):
    matrix.append(list(map(int,input().split())))
for j in range(columns):
    print(*[matrix[i][j] for i in range(rows)])    
