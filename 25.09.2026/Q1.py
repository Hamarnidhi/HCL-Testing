'''A college maintains the daily attendance details of its students in the form of a list containing student IDs. Some students may have attended multiple sessions on the same day. The administration wants to identify the longest continuous sequence of sessions in which no student ID is repeated. Develop a solution that determines the maximum length of such a sequence.'''

def longest_unique_sequence(students):
    seen = set()
    left = 0
    maxlen= 0

    for right in range(len(students)):

        while students[right] in seen:
            seen.remove(students[left])
            left += 1

        seen.add(students[right])

        current = right - left + 1
        maxlen = max(maxlen, current)

    return maxlen

attendance = [101, 102, 103, 102, 104, 105]
answer = longest_unique_sequence(attendance)
print("Longest unique sequence length:", answer)