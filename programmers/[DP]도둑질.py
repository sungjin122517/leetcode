'''
Level 4

우선 원형 생각 하지말고 풀어보자
n = 1,000,000 -> O(n)

원형 생각하면, 아예 dp를 두번 구현해야한다
1. 첫 집이 털렸을 때
2. 첫 집 안 털렸을 때
그리고 최댓값 반환하기
'''

def solution(money):
    dp = [0 for _ in range(len(money))]
    dp[0], dp[1] = money[0], max(money[0], money[1])
    
    # 첫 집 털고 마지막 집 안 털기
    for i in range(2, len(dp)-1):            
        dp[i] = max(dp[i-1], money[i] + dp[i-2])
        
    dp2 = [0 for _ in range(len(money))]
    dp2[0], dp2[1] = 0, money[1]
    
    # 마지막 집 털기
    for i in range(2, len(dp)):            
        dp2[i] = max(dp2[i-1], money[i] + dp2[i-2])
    
    return max(max(dp), max(dp2))