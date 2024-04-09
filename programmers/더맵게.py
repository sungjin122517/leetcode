import heapq

def solution(scoville, K):
    answer = 0
    
    # scoville.sort()
    # count = 0
    # for i in range(len(scoville)-1):
    #     if scoville[i] >= K:
    #         return count
    #     value = scoville[i] + scoville[i+1]*2
    #     scoville[i+1] = value
    #     count += 1
    #     scoville.sort()
    
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        val = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, val)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    
    return answer