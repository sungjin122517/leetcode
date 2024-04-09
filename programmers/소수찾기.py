from itertools import permutations

def isPrime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    perm = []
    result = []

    # 1. 조합
    for i in range(1, len(numbers)+1):
        perm.extend(permutations(numbers, i))   # save all permutations in perm, e.g. [('1', '7'), ('7', '1')]
        # save int value of each permutation in result
        for p in perm:
            result.append(int(''.join(p)))  

    return answer