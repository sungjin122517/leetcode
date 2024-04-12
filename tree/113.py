# 113. Path Sum II

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def dfs(root, total, temp):
            if root is None:
                return
            # temp.append(root.val)
            total += root.val
            temp.append(root.val)

            # if total < targetSum:
            #     temp.append(root.val)
            #     dfs(root.left, total, temp)
            #     dfs(root.right, total, temp)
            # elif total == targetSum:
            #     temp.append(root.val)
            #     ans.append(temp)
            # else:
            #     return

            if total == targetSum and root.left == None and root.right == None:
                ans.append(list(temp))
            else:
                dfs(root.left, total, temp)
                dfs(root.right, total, temp)
            
            # backtracking: 현재 노드 처리 후 temp에서 제거
            # 다음 경로 탐색에 영향을 주지 않기 위함
            temp.pop()
        
        dfs(root, 0, [])
        return ans