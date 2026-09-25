'''A company stores the monthly performance scores of an employee for several months. The scores may contain both positive and 
negative values depending on the employee's performance. Management wants to identify the continuous 
period during which the employee achieved the highest overall performance.'''

arr = [−2, 1, −3, 4, −1, 2, 1, −5, 4]

maxsum = arr[0]

for i in range(len(arr)):
    total = 0

    for j in range(i, len(arr)):
        total += arr[j]

        if total > maxsum:
            maxsum = total

print(maxsum)
