# 300. Longest Increasing Subsequence
# O(n^2)는 생각해냈다

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        # dp[len(nums)-2] = 2 if nums[len(nums)-1] > nums[len(nums)-2] else 1
        # for i in reversed(range(len(nums)-3)):
        #     if nums[i+1] > nums[i]:
        #         dp[i] = dp[i] + dp[i+1]
        #     else:
        #         temp = i+2
        #         while temp < len(nums):
        #             if nums[temp] > nums[i]:
        #                 dp[i] = dp[i] + dp[temp]
        #                 break
        #             temp = temp + 1
        
        # return max(dp)

        for i in range(len(nums) - 2, -1, -1):
            print(i)
            for j in range(i+1, len(nums)):
                # print(j)
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
        
        
        
# main to test my code
if __name__ == "__main__":
    list = [10, 9, 2, 5, 3, 7, 101, 18]
    solution = Solution()
    result = solution.lengthOfLIS(list)
    print(result)