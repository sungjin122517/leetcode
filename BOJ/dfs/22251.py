# 22251. 빌런 호석

'''
n=9 k=1 p=2 x=5
binary? string? list?

해답:
비트마스킹 + dfs 문제
'''

n, k, p, x = map(int, input().split())

# 자릿수 맞춰주기
if len(str(x)) < k:
    cx = '0' * (k-len(str(x))) + str(x)
else:
    cx = str(x)

num = ['1111110', '0110000', '1101101', '1111001', '0110011', '1011011',
       '1011111', '1110000', '1111111', '1111011']
arr = []

# 다른 숫자로 바꿀 때 반전시켜줘야하는 led의 개수 저장
# e.g. arr[1][2] = 5 -> 숫자 1을 2로 바꾸려면 총 5개의 LED를 반전시켜야 한다.
for i in range(10):
    arr.append([])
    for j in range(10):
        if i == j:
            arr[i].append(0)
        else:
            temp = 0
            for a in range(7):
                if num[i][a] != num[j][a]:
                    temp += 1
            arr[i].append(temp)

def dfs(depth, cnt, cx):
    if depth >= len(cx): # 끝까지 다 확인했으면 종료
        if int(cx) == x: # 현재 층수와 결과가 같으면 안 됨
            return 0
        elif 1 <= int(cx) <= n: # 조건에 맞는 경우
            return 1
        else: # 그외 경우는 불가능
            return 0
    
    result, cur = 0, int(cx[depth]) # 정답, 바꿔줄 숫자
    for i in range(10):
        if cur != i and (arr[cur][i] <= cnt): # 남은 반전 가능 횟수보다 필요한 반전 횟수가 작아야 바꿀 수 있음
            dx = cx[:depth] + str(i) + cx[depth+1:]
            result += dfs(depth+1, cnt-arr[cur][i], dx)
        
        elif cur == i:
            result += dfs(depth+1, cnt, cx)
        
    return result

print(dfs(0, p, cx))