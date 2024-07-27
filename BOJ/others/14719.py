# 14719. 빗물

'''
n = 25000 -> O(nlogn)
뭔가 bfs일 거 같은데, visited 표시하는 조건을 모르겠다.
아니면 그냥 2중 루프인가?

알고리즘 분류 확인: 구현, 시뮬레이션

해답:
양 옆에 자신보다 작은 높이의 블록이 있다면 해당 위치는 물이 고일 수 없다.
1. 자기 기준으로 left_max, right_max 구한다
'''

h, w = map(int, input().split())
rain = list(map(int, input().split()))
ans = 0

for i in range(1, w-1):
    left_max = max(rain[:i])
    right_max = max(rain[i+1:])
    
    compare = min(left_max, right_max)
    
    if rain[i] < compare:
        ans += (compare - rain[i])

print(ans)