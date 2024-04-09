from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        row, col = len(image), len(image[0])
        visited = set()
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        num = image[sr][sc]

        def dfs(r, c):
            if (r, c) in visited:
                return
            image[r][c] = color
            visited.add((r, c))

            for direction in directions:
                next_r, next_c = r + direction[0], c + direction[1]
                if 0 <= next_r < row and 0 <= next_c < col and image[next_r][next_c] == num:
                    dfs(next_r, next_c)
        
        dfs(sr, sc)

        return image




