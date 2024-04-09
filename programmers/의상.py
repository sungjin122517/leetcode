def solution(clothes):
    hash_map = {}

    # 종류별로 옷 구분하기
    for clothe, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1

    ans = 1
    for key in hash_map:
        ans *= (hash_map[key] + 1)

    return ans - 1
