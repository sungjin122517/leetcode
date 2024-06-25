# 22233. 가희와 키워드


# 시간 초과
# n, m = map(int, input().split())

# memo = []
# for i in range(n):
#     memo.append(input())

# for j in range(m):
#     keywords = list(map(str, input().split(',')))
#     for word in keywords:
#         if word in memo:
#             memo.remove(word)
#             n -= 1
#     print(n)

'''
list 대신 dictionary 사용하면 search가 O(1) 이니깐 시간 훨씬 덜 걸림
입출력 방식도 바꿔서 시간 줄이기
'''
import sys

n, m = map(int, sys.stdin.readline().split())

memo = {}
for i in range(n):
    memo[sys.stdin.readline().rstrip()] = 1

for j in range(m):
    keywords = list(sys.stdin.readline().rstrip().split(','))
    for word in keywords:
        if word in memo.keys():
            if memo[word] == 1:
                memo[word] = 0
                n -= 1
    print(n)
