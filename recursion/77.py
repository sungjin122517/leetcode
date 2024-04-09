from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def backtrack(start, comb):
            if len(comb) == k:
                print(comb.copy())
                ans.append(comb.copy())
                return
            
            for i in range(start, n+1):
                comb.append(i)
                backtrack(i+1, comb)
                comb.pop()
        
        backtrack(1, [])
        return ans
    

if __name__ == "__main__":
    n = 4
    k = 2
    solution = Solution()
    result = solution.combine(n, k)
    # print(result)
        