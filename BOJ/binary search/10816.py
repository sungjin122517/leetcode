# 10816. 숫자 카드 2: binary search

'''
중복 원소의 개수를 찾기 위해, upper bound와 lower bound의 개념을 활용한다.
lower bound: 찾고자 하는 값 이상의 값이 처음으로 나타나는 위치
upper bound: 찾고자 하는 값을 초과한 값을 처음 만나는 위치
그렇다면 중복 원소의 개수 = ubound - lbound
원소가 존재하지 않는다면 상한, 하한 모두 같은 인덱스를 가리키고 있다. 따라서 0.

https://st-lab.tistory.com/267
'''

import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
card.sort()

m = int(input())
find = list(map(int, input().split()))

# cardDic = {}
# for c in card:
#     if c in cardDic:
#         cardDic[c] += 1
#     else:
#         cardDic[c] = 1

# def binarySearch(num):
#     # cnt = 0
#     start, end = 0, n-1
    
#     while start < end:
#         mid = (start+end)//2
        
#         if card[mid] > num:
#             end = mid - 1
#         elif card[mid] < num:
#             start = mid + 1
#         else:
#             # 숫자가 여러개 있을 때
            
#             return cardDic[card[mid]]
    
#     return 0

# for f in find:
#     print(binarySearch(f), end=' ')

def countOccurrences(num):
    # num이 처음 나타나는 인덱스 찾기
    def lower_bound(num):
        start, end = 0, n
        while start < end:
            mid = (start + end) // 2
            if card[mid] < num:
                start = mid + 1
            else:
                end = mid
        return start

    # num이 마지막으로 나타나는 인덱스 찾기
    def upper_bound(num):
        start, end = 0, n
        while start < end:
            mid = (start + end) // 2
            if card[mid] <= num:
                start = mid + 1
            else:
                end = mid
        return start

    lower = lower_bound(num)
    upper = upper_bound(num)
    return upper - lower

for f in find:
    print(countOccurrences(f), end=' ')