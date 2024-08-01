# 7490. 0 만들기

'''
dp 문제인데, dp 구조 잡는게 감이 안 온다.

알고리즘 분류를 찾아보니: 구현 / 문자열 / 브루트포스 / 백트래킹

https://thought-process-ing.tistory.com/m/330

recursion 활용해서 모든 경우의 수를 [+, -, ' '] 포함하여 string으로 조합한다.
n의 범위가 1에서 9까지이므로, recursion으로 해도 시간복잡도가 크게 증가하지 않는다.
그리고 더해서 0이면 프린트.
'''

cnt = int(input())

def recur(total, sign, num, length, string):
    if length == n:
        total = total + sign*num
        if total == 0:
            print(string)
    else:
        recur(total         , sign, num*10+(length+1), length+1, string+' '+str(length+1))
        recur(total+sign*num, 1   , length+1         , length+1, string+'+'+str(length+1))
        recur(total+sign*num, -1  , length+1         , length+1, string+'-'+str(length+1))

# def calculate(string):
#    string = string.replace(" ", '')
    
for _ in range(cnt):
    n = int(input())
    recur(0, 1, 1, 1, "1")
    print()