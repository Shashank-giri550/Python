"""Problem Statement

Two words are called anagrams if they contain exactly the same characters with the same frequencies,but possibly in a different order. Determine whether the given two words are anagrams.

Input:
listen
silent

Output:
Anagram: Yes
"""

a = input().strip()
b = input().strip()

if sorted(a) == sorted(b):
    print("Anagram: Yes")
else:
    print("Anagram: No")    