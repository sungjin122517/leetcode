# 56. Merge intervals

# Given an array of intevals,
# 1. Merge all overlapping intervals
# 2. Return an array of the non-overlapping intervals that cover all the intervals in the input

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. Sort intervals (merge sort)
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        # 2. Check if two intervals overlap & merge
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                # output[-1] = [min(output[-1][0], start), max(end, lastEnd)]
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        
        return output