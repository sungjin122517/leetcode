# 973. K Closest Points to Origin

# Given an array of points with coordinates [x, y] return the k closest points to the origin
# Use Euclidean distance to calculate the distance

# 1. Create array for distance
# 2. Create min heap & heapify
# 3. Return top k elements

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        # for i in range(len(points)):
        #     # Calculate Euclidean distance
        #     distance = (points[i][0] ** 2 + points[i][1] ** 2) ** 0.5
        #     distances.append({distance : i})
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minHeap.append([distance, x, y])

        heapq.heapify(minHeap)
        result = []
        while k > 0:
            distance, x, y = heapq.heappop(minHeap)
            result.append([x, y])
            k -= 1

        return result


    
        