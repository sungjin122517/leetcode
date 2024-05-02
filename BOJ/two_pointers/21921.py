# 21921. 블로그

n, x = map(int, input().split())
visit = list(map(int, input().split()))

# sum of visit from start to end
# time complexity: O(nx) which leads to 시간초과
sumVisits = sum(visit[:x])
maxVisits = sumVisits
count = 1

start, end = 1, x

while end < n:
    # update sumVisits
    sumVisits = sumVisits - visit[start-1] + visit[end]

    if sumVisits > maxVisits:
        maxVisits = sumVisits
        count = 1
    elif sumVisits == maxVisits:
        count += 1
    start, end = start+1, end+1

if maxVisits == 0:
    print('SAD')
else:
    print(maxVisits)
    print(count)
