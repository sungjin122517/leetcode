def solution(people, limit):

# length of people: max 5,000 -> O(nlogn)

# 1. people 정렬
# 2. index 양쪽 끝에 두고 제일 가벼운 사람 + 제일 무거운 사람 해서 탈 수 있는지 확인

    people.sort()

    left, right = 0, len(people)-1
    count = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1

        count += 1
    
    return count