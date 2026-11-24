"""Problem Staement 

A courier company records the length,width and height of a parcel. Calculate its volume and classify it is a cube if all three dimensions are equal; otherwise,classify it as a cuboid.

Input:
5 5 5

Output:
Volume: 125
Type: Cube
"""
length,width,height = map(int,input().split())

volume = length*width*height

print("Volume:",volume)
if length == width == height: 
    print("Type: Cube")
else:
    print("Type: Cuboid")
     