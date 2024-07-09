# 2179. 비슷한 단어: 문자열 (골드 4)

'''
N개의 영단어들이 주어졌을 때, 가장 비슷한 두 단어를 구해내는 프로그램을 작성하시오.

알고리즘 분류:
- 정렬
- 해시를 사용한 집합과 맵

1. 알파벳별로 우선 정렬하려고 하는데, 그러면 입력 순서대로 프린트 해야하는건 어떡하냐?
2. 해시 자체를 어떻게 활용해야할지

배운점:
- 문자열을 정렬시키면 가장 긴 접두사를 갖고 있는 문자끼리 붙게 된다.

https://velog.io/@jckim22/%EB%B0%B1%EC%A4%80-2179-%EB%B9%84%EC%8A%B7%ED%95%9C-%EB%8B%A8%EC%96%B4-%EA%B5%AC%ED%98%84-%EB%AC%B8%EC%9E%90%EC%97%B4
'''

import sys
input = sys.stdin.readline

num = int(input())
temp = [input().rstrip() for _ in range(num)]

# num = 9
# temp = ["noon", "is", "for", "lunch", "most", "noone", "waits", "until", "two"]

words = sorted(list(enumerate(temp)), key = lambda x: x[1])
# words = [(2, 'for'), (1, 'is'), (3, 'lunch'), (4, 'most'), (0, 'noon'), (5, 'noone'), (8, 'two'), (7, 'until'), (6, 'waits')]

# 두 단어의 같은 접두사 길이 반환
def check(a, b):
    cnt = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            cnt += 1
        else: 
            break
    return cnt

maxLen = -1
idxLen = [0] * num
for i in range(num-1):
    cnt = check(words[i][1], words[i+1][1])
    maxLen = max(maxLen, cnt)
    
    idxLen[words[i][0]] = max(cnt, idxLen[words[i][0]])
    idxLen[words[i+1][0]] = max(cnt, idxLen[words[i+1][0]])
    
first = 0
for i in range(num):
    if first == 0:
        if idxLen[i] == max(idxLen):
            first = temp[i]
            print(first)
            nxt = temp[i][:maxLen]
    else:
        if idxLen[i] == max(idxLen) and temp[i][:maxLen] == nxt:
            print(temp[i])
            break