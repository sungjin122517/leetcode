# 2138. 전구와 스위치

'''
n=100,000 -> O(nlogn)
bfs + 백트래킹?
바꾸기 / 체크하기

해답: greedy
1. 전구를 누르는 순서는 상관이 없다!
- 0부터 n-1 스위치까지 순차적으로 돌면서 눌러도 될지 말지를 결정해라
2. 순차적으로 탐색한다면, i번째 스위치가 i-1번째 전구의 상태를 결정할 마지막 스위치이다.
'''

n = int(input())
start = list(map(bool, map(int, input().rstrip())))
end = list(map(bool, map(int, input().rstrip())))

firstPress = start.copy()
firstPress[0] = not firstPress[0]
firstPress[1] = not firstPress[1]

# print(start)
# print(end)

def change(arr, cnt):
    for i in range(1, n-1):
        if arr[i-1] != end[i-1]:
            cnt += 1
            arr[i-1] = not arr[i-1]
            arr[i] = not arr[i]
            arr[i+1] = not arr[i+1]
    
    # 마지막 전구만 따로 처리
    if arr[n-1] != end[n-1]:
        cnt += 1
        arr[n-2] = not arr[n-2]
        arr[n-1] = not arr[n-1]
    
    if arr == end:
        return cnt
    else:
        return -1

if start == end:
    print(0)
else:
    # 첫 번째 전구를 누르지 않는 경우
    cnt = change(start, 0)
    if cnt != -1:
        print(cnt)
    else:
        # 첫 번째 전구를 누르는 경우
        cnt = change(firstPress, 1)
        print(cnt if cnt else -1)