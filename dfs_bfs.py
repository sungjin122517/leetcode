from collections import deque

# matrix bfs
def bfs(matrix):
    if not matrix:
        return []
    
    visited = set()
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    row, col = len(matrix), len(matrix[0])

    def traverse(i, j):
        # create queue
        queue = deque()
        queue.append((i, j))
        while queue:
            # visited 처리
            curr_i, curr_j = queue.popleft()
            if (curr_i, curr_j) not in visited:
                visited.add((curr_i, curr_j))
                # check four directions
                for dir in directions:
                    next_i, next_j = curr_i+dir[0], curr_j+dir[1]
                    if 0 <= next_i < row and 0<= next_j < col:
                        queue.append((next_i, next_j))

    for i in range(row):
        for j in range(col):
            traverse(i, j)

# 2d list graph bfs
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

# tree bfs
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root):
    if root is None:
        return
    
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# matrix dfs
def dfs(matrix):
    if not matrix:
        return []
    
    visited = set()
    rows, cols = len(matrix), len(matrix[0])
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def traverse(i, j):
        if (i, j) in visited:
            return
        
        visited.add((i, j))
        for dir in directions:
            next_i, next_j = i + dir[0], j + dir[1]
            if 0 <= next_i < rows and 0 <= next_j < cols:
                # Add in question-specific checks, where relevant.
                traverse(next_i, next_j)
    
    for i in range(rows):
        for j in range(cols):
            traverse(i, j)

# 2d list graph dfs
def dfs(graph, start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

# tree dfs
def dfs(root):
    if root is None:
        return
    dfs(root.left)
    dfs(root.right)

        


