from collections import deque

def solution(maps):
#     if not maps:
#         return -1
    
    # visited = set()
    rows, cols = len(maps), len(maps[0])
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    
    def traverse(i, j):
        queue = deque()
        queue.append((i, j))
        
        while queue:
            curr_i, curr_j = queue.popleft()
            for dir in directions:
                next_i, next_j = curr_i+dir[0], curr_j+dir[1]
                if 0 <= next_i < rows and 0 <= next_j < cols and maps[next_i][next_j] == 1:
                    maps[next_i][next_j] = maps[curr_i][curr_j] + 1
                    queue.append((next_i, next_j))
                    
        return maps[rows-1][cols-1]
    
    answer = traverse(0, 0)
    return -1 if answer == 1 else answer