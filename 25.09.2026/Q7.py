''' Bank Transaction Analysis A bank stores transaction amounts for a customer's account.
 A continuous group of transactions may add up to a specific target amount.
 The auditing system needs to determine how many different continuous transaction
  groups produce exactly the specified amount.
'''

arr = [1, 2, 3, 2, 1]
target = 5

count = 0

for i in range(len(arr)):
    total = 0

    for j in range(i, len(arr)):
        total += arr[j]

        if total == target:
            count += 1

print(count)
