# 130. Surrounding regions

from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        if rows <= 2 or cols <= 2:
            return
        
        queue = deque()

        for row in range(rows):
            queue.append((row, 0))
            queue.append((row, cols-1))

        for col in range(cols):
            queue.append((0, col))
            queue.append((rows-1, col))
        
        while queue:
            x, y = queue.popleft()
            if x >= 0 and x < rows and y >= 0 and y < cols and board[x][y] == "O":
                board[x][y] = "T"
                queue.append((x+1, y))
                queue.append((x-1, y))
                queue.append((x, y+1))
                queue.append((x, y-1))
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "T":
                    board[row][col] = "O"

        # visited = set()
        # rows, cols = len(board), len(board[0])

        # def bfs(board, x, y):
        #     queue = deque()
        #     queue.append((x, y))
        #     while queue:
        #         curr_i, curr_j = queue.popleft()
        #         if (curr_i, curr_j) not in visited:
        #             visited.add((curr_i, curr_j))
        #             if board[curr_i][curr_j] == "O":
        #                 right = (curr_i + 1, curr_j)
        #                 left = (curr_i - 1, curr_j)
        #                 up = (curr_i, curr_j + 1)
        #                 down = (curr_i, curr_j - 1)
        #                 if (board[right[0]][right[1]] == "X" or right[0] == len(board[0])) and (board[left[0]][left[1]] == "X" or left[0] < 0) and (board[up[0]][up[1]] == "X" or up[1] < 0) and (board[down[0]][down[1]] == "X" or down[1] == len(board)):
        #                     continue
        #                 else:
        #                     board[curr_i][curr_j] = "X"
        #                 queue.append()


