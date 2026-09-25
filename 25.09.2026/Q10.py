'''A hospital receives appointment requests represented by starting and ending times.
 Some appointments overlap with each other. The scheduling system needs to combine 
 overlapping appointment periods so that the final schedule contains only 
 non-overlapping time ranges.'''

arr = [[1,3], [2,6], [8,10], [9,12]]
arr.sort()
result = []
for inte in arr:
    if not result or result[-1][1] < inte[0]:
        result.append(inte)
    else:
        result[-1][1] = max(result[-1][1], inte[1])
print(result)
