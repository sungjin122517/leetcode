# 2467. 용액

'''
산성 용액(양의 정수), 알칼리성 용액(음의 정수)
합쳐서 0에 가장 가까운 용액 만들기
정렬된 순서로 주어진다

n: 100,000 -> O(nlogn)

two pointer? O

해답:
- 합이 0보다 작으면, left += 1
- 합이 0보다 크면, right -= 1

'''

import sys
input = sys.stdin.readline

n = int(input())
sol = list(map(int, input().split()))

# two pointer
left, right = 0, len(sol)-1
x, y = sol[left], sol[right]
val = abs(sol[left] + sol[right])

while left < right:
    add = sol[left] + sol[right]
    
    if abs(add) < val:
        val = abs(add)
        x, y = sol[left], sol[right]
    
    if add < 0:
        left += 1
    else:
        right -= 1

print(x, y)



# if all positive

# if all negative

# idx = 0
# while sol[idx] <= 0:
#     idx += 1

# neg = sol[:idx]
# neg.sort(key=lambda x:-x)
# pos = sol[idx:]
# val = 1e9 + 1
# x, y = 0, 0
# print(pos)

# for j in range(len(neg)):
#     for i in range(len(pos)):
#         add = abs(neg[j] + pos[i])
#         print(add)

#         if add < val:
#             val = add
#             x, y = neg[j], pos[i]
#             print('if: ', val)
#         else:
#             print('else: ', val)
#             break

# print(x, y)