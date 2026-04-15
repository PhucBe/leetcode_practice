"""
Problem: 2352. Equal Row and Column Pairs
Link: https://leetcode.com/problems/equal-row-and-column-pairs/
Difficulty: Medium
Topics: Array, Hash Table, Matrix, Counting

Idea:
- Mỗi hàng là một dãy số
- Mỗi cột cũng là một dãy số
- Ta cần đếm số cặp (row, col) sao cho dãy của hàng bằng đúng dãy của cột
- Biến mỗi hàng thành tuple để dùng làm key trong hash map
- Đếm số lần xuất hiện của từng hàng
- Với mỗi cột, tạo tuple tương ứng rồi xem nó xuất hiện bao nhiêu lần trong các hàng
- Cộng dồn kết quả

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""
from typing import List
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_count = Counter(tuple(row) for row in grid)
        n = len(grid)
        ans = 0

        for col in range(n):
            col_values = tuple(grid[row][col] for row in range(n))
            ans += row_count[col_values]

        return ans