"""
Problem: 724. Find Pivot Index
Link: https://leetcode.com/problems/find-pivot-index/
Difficulty: Easy
Topics: Array, Prefix Sum

Idea:
- Tổng bên trái của mỗi vị trí có thể được tính khi duyệt mảng
- Tổng bên phải = tổng toàn mảng - giá trị hiện tại - tổng bên trái
- Với mỗi index:
    + nếu left_sum == right_sum thì đó là pivot index
- Vì cần lấy pivot bên trái nhất, chỉ cần gặp vị trí đầu tiên thỏa mãn là return luôn

Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            right_sum = total_sum - left_sum - num

            if left_sum == right_sum:
                return i

            left_sum += num

        return -1