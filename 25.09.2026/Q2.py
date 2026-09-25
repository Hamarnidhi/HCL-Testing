'''An online shopping application stores the prices of products viewed by a customer during a browsing session. The customer wants to identify a continuous range of products that provides the maximum possible total discount value. Given the discount values, determine the maximum value that can be obtained from any continuous range.'''

def max_dis(dis):
    current_sum = dis[0]
    max_sum = dis[0]

    for value in dis[1:]:
        current_sum = max(value, current_sum + value)
        max_sum = max(max_sum, current_sum)
    return max_sum

dis = [10, -5, 20, -10, 30]
result = max_dis(dis)
print(result)