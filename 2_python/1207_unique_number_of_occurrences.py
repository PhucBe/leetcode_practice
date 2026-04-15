"""
Problem: 1207. Unique Number of Occurrences
Link: https://leetcode.com/problems/unique-number-of-occurrences/
Difficulty: Easy
Topics: Array, Hash Table

Idea:
- Dùng dict để đếm số lần xuất hiện của từng giá trị
- Lấy các tần suất ra
- Nếu số lượng tần suất bằng số lượng phần tử trong set của tần suất,
  nghĩa là tất cả tần suất đều unique

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        counts = freq.values()
        return len(counts) == len(set(counts))