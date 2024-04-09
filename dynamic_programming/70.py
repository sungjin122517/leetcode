class Solution:
    def climbStairs(self, n: int) -> int:
        # Bottom up
        # We just need two variables
        first, second = 1, 1
        for i in range(n-1):
            temp = first
            first = first + second
            second = temp
        
        return first
