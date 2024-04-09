from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []

        row, col = len(mat), len(mat[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        result = []
        MAX_VALUE = row*col
        queue = deque()

        # initialize 2d list of zeros
        for i in range(row):
            result.append([])
            for j in range(col):
                if mat[i][j] == 0:
                    result[i].append(0)
                    queue.append((i, j))
                else:
                    result[i].append(MAX_VALUE)
        
        while queue:
            curr_r, curr_c = queue.popleft()
            for direction in directions:
                next_r, next_c = curr_r + direction[0], curr_c + direction[1]
                if 0 <= next_r < row and 0 <= next_c < col and result[next_r][next_c] > result[curr_r][curr_c] + 1:
                    result[next_r][next_c] = result[curr_r][curr_c] + 1
                    queue.append((next_r, next_c))

        return result



