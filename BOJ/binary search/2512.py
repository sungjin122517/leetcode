# 2512. 예산

n = int(input())
budgets = list(map(int, input().split()))
# budgets.sort()
m = int(input())

# if sum(budgets) < total:
#     print(budgets[-1]) 
# else:

low, high = 0, max(budgets)

answer = 0
while low <= high:
    total = 0
    # print('low:', low)
    # print('high:', high)
    mid = (low + high) // 2
    # print('mid:', mid)

    for budget in budgets:
        total += min(mid, budget)
        # print('total:', total)
    
    if total <= m:
        low = mid + 1
        answer = mid
        # print('answer:', answer)
    
    else:
        high = mid - 1

print(answer)




