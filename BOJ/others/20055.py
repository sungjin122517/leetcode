# 20055. 컨베이어 벨트 위의 로봇

'''
fixed list 놔두고 start, end index 유지
로봇의 위치도 index로 유지
근데 여러개의 로봇이 더해질텐데 그냥 list로 유지해도 되나?

해답
- 맨 먼저 올라간 로봇이 당연히 end 위치와 가깝다. 따라서 end에서 부터 start까지 인덱스를 감소시키며 확인해준다.

https://velog.io/@isayaksh/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-BOJ-20055-%EC%BB%A8%EB%B2%A0%EC%9D%B4%EC%96%B4-%EB%B2%A8%ED%8A%B8-%EC%9C%84%EC%9D%98-%EB%A1%9C%EB%B4%87-Python
'''

n, k = map(int, input().split())
belt = list(map(int, input().split()))
robot = [False] * (n*2)

start, end = 0, n-1
cnt = 0

while True:
    cnt += 1
    
    # step 1
    start = start - 1 if start - 1 >= 0 else 2*n - 1
    robot[end] = False
    end = end - 1 if end - 1 >= 0 else 2*n - 1

    
     
    # step 2
    # if hasRobot:
    #     idx = end
    idx = end
    for i in range(n):
        if robot[idx]:
            if idx == end:
                robot[idx] = False 
            else:
                nxt = idx + 1 if idx + 1 < 2*n else 0
                if not robot[nxt] and belt[nxt] > 0:
                    robot[idx] = False
                    robot[nxt] = True
                    belt[nxt] -= 1
        idx = idx - 1 if idx - 1 >= 0 else 2*n - 1
    
    # step 3
    if belt[start] > 0 and not robot[start]:
        belt[start] -= 1
        # if belt[start] == 0:
        #     cnt += 1
        #     if cnt >= k:
        #         stop = True
        robot[start] = True # 로봇 시작 위치에 올림
    
    # if stop:
    #     break
    if belt.count(0) >= k:
        break

print(cnt)