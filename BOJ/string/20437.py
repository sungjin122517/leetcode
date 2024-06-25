# 20437. 문자열 게임 2: string

'''
N = 10,000 -> O(nlogn)

two pointer? 너무 오래 걸릴거 같다.

정답:
1. 전체 문자열을 돌면서 각 문자의 갯수를 세고 dictionary에 저장한다
2. 다시 문자열을 돌아서 해당 문자가 k개 이상인 경우 index 저장
3. 인덱스 활용해서 min, max 찾기

배운점:
- list object is not iterable
'''

import sys

num = int(sys.stdin.readline())
for _ in range(num):
    w = sys.stdin.readline()
    k = int(input())

    maxLen, minLen = 0, len(w)
    check = False # 결과 유무 확인용

    # 1. 문자 갯수 저장
    chars = {}
    # for i in range(len(w)):
    #     if w[i] in chars:
    #         chars[w[i]] += 1
    #     else:
    #         chars[w[i]] = 1
    for char in w:
        chars[char] = chars.get(char, 0) + 1

    # 2. index 저장
    indexes = {}
    for i in range(len(w)):
        if chars[w[i]] < k:
            continue
        
        check = True
        indexes[w[i]] = indexes.get(w[i], []) + [i]

    # 3. min, max 찾기
    # for idxList in indexes.values:
    #     start, end = 0, k-1
    #     while end < len(idxList):
    #         minLen = min(idxList[end]-idxList[start]+1, minLen)
    #         maxLen = max(idxList[end]-idxList[start]+1, maxLen)
    #         start += 1
    #         end += 1
    for key, value_list in indexes.items():
        start, end = 0, k-1
        while end < len(value_list):
            minLen = min(value_list[end]-value_list[start]+1, minLen)
            maxLen = max(value_list[end]-value_list[start]+1, maxLen)
            start += 1
            end += 1
    
    if check:
        print(minLen, maxLen)
    else:
        print(-1)





