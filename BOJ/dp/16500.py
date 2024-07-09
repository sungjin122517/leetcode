# 16500. 문자열 판별: dp

'''
알파벳 소문자로 이루어진 문자열 S와 단어 목록 A가 주어졌을 때, S를 A에 포함된 문자열을 한 개 이상 공백없이 붙여서 
만들 수 있는지 없는지 구하는 프로그램을 작성하시오. A에 포함된 단어를 여러 번 사용할 수 있다.
A에 포함된 문자열로 S를 만들 수 있으면 1, 없으면 0을 출력한다.

[software, contest]
-> softwarecontest

https://velog.io/@dosadola/python-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%8C%90%EB%B3%84-%EB%B0%B1%EC%A4%80-16500
'''

import sys
input = sys.stdin.readline

s = input().rstrip()
num = int(input())
words = [input().rstrip() for _ in range(num)]
dp = [0] * (len(s)+1)
dp[0] = 1

for i in range(len(s) + 1):
    for w in words:
        wordLen = len(w)
        if i >= wordLen and dp[i - wordLen] == 1 and s[i-wordLen:i] == w:
            dp[i] = 1

print(dp)
if dp[len(s)]:
    print(1)
else:
    print(0)