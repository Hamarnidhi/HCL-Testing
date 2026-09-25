'''A network monitoring system receives packet identifiers in chronological order. 
The system must determine the longest sequence of consecutive packets whose identifiers 
form a continuous numerical sequence, regardless of their original order in the incoming
 data.'''
arr = [100, 4, 200, 1, 3, 2]

arr.sort()

max_count = 1
count = 1

for i in range(1, len(arr)):
    if arr[i] == arr[i - 1] + 1:
        count += 1
    elif arr[i] == arr[i - 1]:
        continue
    else:
        count = 1

    if count > max_count:
        max_count = count

print(max_count)
