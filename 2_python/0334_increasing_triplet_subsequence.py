"""
Problem: 334. Increasing Triplet Subsequence
Link: https://leetcode.com/problems/increasing-triplet-subsequence/
Difficulty: Medium
Topics: Array, Greedy

Idea:
- Ta chỉ cần theo dõi 2 giá trị nhỏ nhất có thể:
    + first: số nhỏ nhất đã gặp
    + second: số nhỏ nhất lớn hơn first đã gặp
- Duyệt từng số trong mảng:
    + Nếu số hiện tại <= first, cập nhật first
    + Ngược lại nếu số hiện tại <= second, cập nhật second
    + Ngược lại, nếu số hiện tại > second thì ta đã có:
        first < second < num
      => tồn tại increasing triplet
- Nếu duyệt hết mà không tìm thấy thì trả về False

Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False