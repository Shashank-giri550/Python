"""Problem Statement
A music application stores song IDs in a playlist. Rotate the playlist to the right by k positions and display the updated order.

Input:
5 2 
1 2 3 4 5

Output:
Playlist: 4 5 1 2 3
"""

n,k = map(int,input().split())
songs = list(map(int,input().split()))

k = k%n
rotated = songs[-k:]+songs[:-k] if k else songs
print("Playlist:",*rotated)    