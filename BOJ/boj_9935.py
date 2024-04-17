# 백준 9935. 문자열 폭발

# 폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다.

# O(n) 시간 복잡도로 풀어야할듯?

target = input()
explosive = input()

# for loop을 돌려서 stack에 target의 char 하나씩 담는다. 근데 어떻게 제외해야할지 감이 안 온다.

stack = []
for char in target:
    stack.append(char)
    # 폭발 문자열이 stack의 끝에 있는지 확인
    # -len(explosive): stack의 끝에서부터 explosive의 길이만큼을 의미
    # stack[-len(explosive):]은 stack의 끝에서부터 explosive의 길이만큼의 문자열을 의미
    if stack[-len(explosive):] == list(explosive):
        for _ in range(len(explosive)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')

# time complexity
# 안쪽에 있는 for loop은 explosive의 길이가 최대 36으로 작기 때문에 상수 시간 안에 수행될 수 있다
# 따라서 O(n) 시간 복잡도를 가진다.

# space complexity
# target의 길이만큼 stack에 쌓이기 때문에 O(n) 공간 복잡도를 가진다.