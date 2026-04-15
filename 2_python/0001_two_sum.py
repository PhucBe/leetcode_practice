"""
Problem: 0001. Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Toppics: Array, Hash Table

Idea:
- Duyệt mảng một lần
- Với mỗi phần tử num, tính complement = target - num
- Kiểm tra complement đã có trong hash map chưa
- Nếu có thì trả về index
- Nếu chưa thì lưu num vào hash map

Time Complexity: O(n)
Space Complexity: O(n)

Notes:
- Phải phân biệt rõ value và index
- Hash map giúp giảm từ O(n^2) -> O(n)
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i