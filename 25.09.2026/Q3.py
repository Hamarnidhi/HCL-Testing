'''A city installs buildings of different heights along a straight road.
 During rainfall, water gets collected between taller buildings.
 The engineering team needs to calculate the total amount of water
 that can remain trapped after heavy rainfall based on the heights of
  the buildings.'''
from math import inf

arr = [1, 1]

l = 0
r = len(arr) - 1
maxar = 0

while l < r:
    length = min(arr[l], arr[r])
    breadth = r - l

    area = length * breadth

    maxar = max(maxar, area)

    if arr[l] < arr[r]:
        l += 1
    else:
        r -= 1

print(maxar)
