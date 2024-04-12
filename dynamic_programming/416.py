# 416. Partition Equal Subset Sum

# sort는 의미가 없을거 같다
# list 2개 두고 하나씩 담기?

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        # 1. target = sum(nums) / 2
        target = sum(nums) // 2
        # initialize dp list with False
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = dp[j] or dp[j-num]

        return dp[target]