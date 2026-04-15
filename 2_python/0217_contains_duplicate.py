"""
Problem: 0217. Contains Duplicate
Link:
Difficulty: Easy
Toppics: Array, Hash Table, Sorting

Idea:
- 
- 
- 
- 

Time Complexity: O(n)
Space Complexity: O(n)

Notes:
-
-
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False