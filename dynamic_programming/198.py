from typing import List

class Solution:
    # this is not dp
    def rob(self, nums: List[int]) -> int:
        dp = nums.copy()
        ans = 0

        for i in range(len(dp)):
            max = dp[i]
            for j in reversed(range(i-1)):
                if max < nums[i] + dp[j]:
                    max = nums[i] + dp[j]
                    dp[i] = max
            if ans < max:
                ans = max
        
        print(dp)
        
        return ans
    
    def rob2(self, nums: List[int]) -> int:
        first, second = 0, 0
        
        for n in nums:
            temp = max(n+first, second)
            first = second
            second = temp
        return second
    


if __name__ == "__main__":
    list = [2, 7, 9, 3, 1]
    solution = Solution()
    result = solution.rob(list)
    print(result)