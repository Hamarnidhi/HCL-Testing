'''A retail company stores the daily sales quantity of a product for several consecutive days. Due to seasonal changes, some days may have negative adjustments. 
The company wants to identify the period that produced the highest multiplication of 
sales-related values. Develop a solution to determine this maximum product.'''
arr = [2, 3, -2, 4]

max_product = arr[0]

for i in range(len(arr)):
    product = 1

    for j in range(i, len(arr)):
        product *= arr[j]

        if product > max_product:
            max_product = product

print(max_product)
