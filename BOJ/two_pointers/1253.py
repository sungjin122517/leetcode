# 1253. 좋다

'''
n=2000 -> O(n^2)

숫자의 값을 인덱스로 정해서 리스트에 저장하면, 메모리 초과가 나려나?
숫자 최댓값은 10억이다.

안 되는거 같다.

https://ppirae.tistory.com/112

해답:
내가 푼 풀이는 end를 start+1로 둔 방식인데, 이렇게 하면 시간초과가 난다.
대신 start=0, end=n-1로 두고 풀어보자.
정렬했기 떄문에, 양쪽 끝에서 start와 end를 중앙으로 이동시키면서 풀면 된다.
그리고 조건에 따라서 start를 우측 이동하던지, end를 좌측 이동하던지 하면 된다.
'''

n = int(input())
good = list(map(int, input().split()))
good.sort()

cnt = 0
for i in range(n):
    # start, end = 0, 1
    
    # while start < n-1:
    #     if start == i:
    #         start += 1
    #         end = start + 1
    #         continue
    #     if end == i:
    #         end += 1
    #         continue
        
    #     if good[start] + good[end] > good[i]:
    #         start += 1
    #         end = start + 1
    #     elif good[start] + good[end] < good[i]:
    #         end += 1
    #     else:
    #         cnt += 1
    #         break

    start, end = 0, n-1
    while start < end:
        if start == i:
            start += 1
            continue
        if end == i:
            end -= 1
            continue

        if good[start] + good[end] == good[i]:
            cnt += 1
            break
        elif good[start] + good[end] < good[i]:
            start += 1
        elif good[start] + good[end] > good[i]:
            end -= 1
    
print(cnt)