# [BOJ] 주식

iter = int(input())

for i in range(iter):
    num = int(input())
    prices = list(map(int, input().split()))

    profit = 0
    maxPrice = 0
    for j in range(num-1, -1, -1):
        if maxPrice > prices[j]:
            profit += maxPrice -  prices[j]
        else:
            maxPrice = prices[j]
    
    print(profit)


# LIG넥스원 코테 2번 문제

# dollarPrice = [1200, 1000, 1100, 1200, 900, 700, 1000, 1200]

# def maxProfit(prices):
#     profit = 0
#     money = 1000
#     numDollar = 0

#     for i in range(len(dollarPrice) - 1):
#         maxPrice = 0
#         minPrice = float('inf')
#         # sell stock
#         if numDollar > 0:
#             maxPrice = prices[i]
#             if maxPrice > prices[i+1]:
#                 money += maxPrice
#                 numDollar -= 1
#                 maxPrice = 0
#         else:
#             # buy stock
#             minPrice = prices[i]
#             if money >= minPrice:
#                 if minPrice < prices[i+1]:
#                     money -= minPrice
#                     numDollar += 1
#                     minPrice = float('inf')
        
#         print("dollar: " + str(numDollar) + " money: " + str(money))
        

        
#     if numDollar > 0:
#         money += prices[len(dollarPrice) - 1] * numDollar
    
#     return money - 1000
            

# print(maxProfit(dollarPrice))
