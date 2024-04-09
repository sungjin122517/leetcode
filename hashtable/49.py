# 49. Group Anagrams
from collections import defaultdict
from typing import List

# take each string and sort: m * nlogn (n: length of string, m: length of list)

# use hashmap -> O(m*n*26)
# key: [eat, tea, ate]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # this enables key without value to be empty list
        result = defaultdict(list) # mapping charCount to list of anagrams

        for str in strs:
            count = [0] * 26 # a ... z

            for char in str:
                count[ord(char) - ord("a")] += 1 # ord gives us ASCII value

            # in python, list cannot be keys because the key must be unique and immutable, so convert list to tuple
            result[tuple(count)].append(str)
        
        return result.values()
            
