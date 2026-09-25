'''An e-commerce application stores the product IDs purchased by a customer in chronological
 order. The same product may appear multiple times. The system needs to 
 determine the longest sequence of consecutive purchases in which every product ID is unique.'''


def longest_unique_purchase(products):
    seen = set()
    left = 0
    maxlen = 0

    for right in range(len(products)):
        while products[right] in seen:
            seen.remove(products[left])
            left += 1

        seen.add(products[right])
        currentlen= right - left + 1
        maxlen = max(maxlen, currentlen)
    return maxlen

products = [10, 20, 30, 20, 40, 50]
result = longest_unique_purchase(products)
print(result)