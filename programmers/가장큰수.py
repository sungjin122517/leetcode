def solution(numbers):
    # 1. sort by first digit

    # 2. 

    answer = ''
    
    numbers = list(map(str, numbers)) # 숫자 배열을 리스트로 만들기
    numbers.sort(key = lambda x : x*3, reverse=True)

    for i in numbers:
        answer += i
    
    # 그냥 answer return 하면 앞에 000이 붙어도 제거해주지 않는다
    return str(int(answer))