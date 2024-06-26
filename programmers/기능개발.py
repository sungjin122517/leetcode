from collections import deque

def solution(progresses, speeds):
    answer = []
    count = 0
    time = 0
    # queue = deque()
    # for i in range(len(progresses)):
    #     queue.append(progresses[i])
    
    # while queue:
    #     count = 0
    #     for i in range(len(progresses)):
    #         queue[i] += speeds[i]
        
    #     while queue and queue[0] >= 100:
    #         queue.popleft()
    #         count += 1
        
    #     answer.append(count)

    while progresses:
        if progresses[0] + time*speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
        
    
    return answer
