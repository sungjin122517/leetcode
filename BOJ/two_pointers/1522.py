# 1522. 문자열 교환: 슬라이딩 윈도우

'''
슬라이딩 윈도우 vs 투 포인터
- 슬라이딩: 항상 구간의 넓이가 고정되어 있음
- 투 포인터: 구간의 넓이가 조건에 따라 유동적으로 변함

해답: 투 포인터 + 슬라이딩 윈도우
- a의 갯수만큼 범위를 설정하고, 해당 범위 안에 b가 제일 적을 때의 b의 갯수를 구하면 된다.

abababababababa
1. (abababab)abababa -> 괄호 안에 b 4개 밖에랑 교환
2. a(babababa)bababa -> 괄호 안에 b 4개 밖에랑 교환
...
15. abababa)bababab(a -> 괄호 안에 b 3개
'''

import sys

text = input()

aCnt = text.count('a')
# bCnt = len(text) - aCnt

start, end = 0, aCnt - 1
bCnt = 0
for i in range(aCnt):
    if text[i] == 'b':
        bCnt += 1

minCnt = bCnt

while start < len(text):
    if text[start] == 'b':
        bCnt -= 1
    start += 1
    
    end += 1
    if text[end % len(text)] == 'b':
        bCnt += 1
        
    minCnt = min(minCnt, bCnt)

print(minCnt)