def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] < i+1:
            return i

    # return all if all numbers are equal
    return len(citations)