# 33. Search in Rotated Sorted Array

# target runtime: O(log n)

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search?
        l, r = 0, len(nums)-1

        # python difference between / and //
        # / -> returns float
        # // -> returns int
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else: # target < mid and target > leftmost
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else: # target > mid and target < rightmost
                    l = mid + 1
        
        return -1