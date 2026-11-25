"""PROBLEM STATEMENT

Convert the entire filename to lowercase. remove leading and trailing spaces,and replace every internal space with an underscore. The file extension must also be converted to lowercase and retained.

Input:
My Project File.txt

Output:
my_project_file.txt
"""
file_name = input().strip()
temp = file_name.lower().replace(" ","_")
print(temp)