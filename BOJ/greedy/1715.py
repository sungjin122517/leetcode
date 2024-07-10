# 1715. 카드 정렬하기: greedy

'''
greedy면 무조건 작은 순서대로 더하면 되는건가? X
반례: 
10, 10, 10, 10 일때,
10+10 + 20+10 + 30+10 = 90
10+10 + 10+10 + 20+20 = 80

정답: 우선순위 큐 사용
[10, 20, 30, 40]
-> [30, 30, 40]
-> [40, 60]
-> [100]
total = 각 스텝에서 가장 작은 수 두 개를 더해서 나온 수들을 더한 값이 최종적인 최소 비교 횟수
마지막에는 수가 하나만 남는걸 생각해라

https://velog.io/@leeeeeyeon/BOJ-1715-%EC%B9%B4%EB%93%9C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0
'''

import sys
import heapq
input = sys.stdin.readline

num = int(input())
cards = []
for _ in range(num):
    # cards.append(int(input()))
    heapq.heappush(cards, int(input()))
# cards.sort()

total = 0
# for i in range(len(cards)-1):
#     total += cards[i] + cards[i+1]
#     cards[i+1] += cards[i]
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    temp = a+b
    # print(temp)
    total += temp
    heapq.heappush(cards, temp)

print(total)