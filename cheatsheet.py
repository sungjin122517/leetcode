# stack/queue
from collections import deque
queue = deque()

# technical tip
# 직접 input 받을 때: list, map 사용

# 공백을 기준으로 구분된 데이터를 입력 받을 때
data = list(map(int, input().split()))

# 공백을 기준으로 구분된 데이터가 많지 않다면
a, b, c = map(int, input().split())

# sys stdin을 활용해 입출력
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = input()             # "1" 입력
print(list(n))          # ['1', '\n']
print([int(n)])         # [1]
print(list(n.rstrip())) # ['1']


# 2d list transpose
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = list(map(list, zip(*mylist)))


# map 활용하기
# list element 모두 int로 형 변환
list(map(int, ['1', '2', '3'])) # [1, 2, 3]

a = list(map(str, range(10))) # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# 2차원 배열 1차원으로 변경
array = [[1, 2], [3, 4], [5, 6]]
print(sum(array, [])) # [1, 2, 3, 4, 5, 6]


# list에서 문자 등장 개수 세기
import collections
answer = collections.Counter(['a', 'b', 'c', 'a', 'b', 'a']) # Counter({'a': 3, 'b': 2, 'c': 1})
print(answer['a']) # 3
print(answer['b']) # 2
print(answer['c']) # 1


# swap
a = 3
b = 4
a, b = b, a


# 무한대와 비교하기
min_val = float('inf')
max_val = float('-inf')


# permutations and combinations
from itertools import permutations, combinations, product
items = ['1', '2', '3']
print(list(permutations(items, 2))) # [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
print(list(combinations(items, 2))) # [('1', '2'), ('1', '3'), ('2', '3')]
# convert combination list elements to int

# 두 개 이상의 리스트에서 모든 조합
items = [['a', 'b', 'c,'], ['1', '2', '3', '4'], ['!', '@', '#']]
print(list(product(*items))) # [('a', '1', '!'), ('a', '1', '@'), ('a', '1', '#'), ('a', '2', '!'), ('a', '2', '@'), ('a', '2', '#'), ...