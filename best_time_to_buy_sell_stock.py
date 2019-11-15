# Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

input1 = [7,1,5,3,6,4]
input2 = [1,2,3,4,5]
input3 = [7,6,4,3,1]


def max_profit(prices):
    max_profit = 0

    for i in range(len(prices)-1):
        if (prices[i] < prices [i+1]):
            diff = prices[i+1] - prices[i]
            max_profit += diff

    return max_profit


print(max_profit(input1))  # 7
print(max_profit(input2))  # 4
print(max_profit(input3))  # 0