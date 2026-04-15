"""
Problem: 2215. Find the Difference of Two Arrays
Link: https://leetcode.com/problems/find-the-difference-of-two-arrays/
Difficulty: Easy
Topics: Array, Hash Table, Set

Idea:
- Dùng set để loại phần tử trùng
- Lấy hiệu hai tập hợp:
  + set(nums1) - set(nums2)
  + set(nums2) - set(nums1)

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        return [list(set1 - set2), list(set2 - set1)]