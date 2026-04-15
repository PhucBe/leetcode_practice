"""
Problem: 0238. Product of Array Except Self
Link:
Difficulty: Medium
Toppics: Array

Idea:
- 
- 
- 
- 

Time Complexity: O(n)
Space Complexity: O(1) extra space (excluding output array)

Notes:
-
-
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        answer = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            answer[i] = prefix[i] * suffix[i]

        return answer

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # answer[i] sẽ chứa prefix product
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        # right lưu suffix product
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer