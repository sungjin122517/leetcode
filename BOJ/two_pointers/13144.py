# 13144. List of Unique Numbers: two pointers

'''
길이가 N인 수열이 주어질 때, 수열에서 연속한 1개 이상의 수를 뽑았을 때 같은 수가 여러 번 등장하지 않는 
경우의 수를 구하는 프로그램을 작성하여라.

1<N<100,000 -> O(nlogn)
'''

num = int(input())
seq = list(map(int, input().split()))

start, end = 0, 0
count = 0

# while start < num:
#     l = [seq[start]]
#     end = start
#     while seq[end] not in l:
#         count += 1
#         end += 1
#     start += 1

# print(count)

visited = [0] * 100001

for i in range(num):
    while end < num:
        if visited[seq[end]]:
            break
        visited[seq[end]] = 1
        end += 1
    
    count += (end - i)
    visited[seq[i]] = 0

print(count)
