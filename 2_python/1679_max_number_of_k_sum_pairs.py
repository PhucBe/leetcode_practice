"""
Problem: 1679. Max Number of K-Sum Pairs
Link: https://leetcode.com/problems/max-number-of-k-sum-pairs/
Difficulty: Medium
Topics: Array, Hash Table, Two Pointers, Sorting

Idea:
- Mỗi lần chọn 2 số có tổng bằng k rồi xóa đi
- Để tối đa số phép toán, ta chỉ cần ghép được càng nhiều cặp hợp lệ càng tốt
- Dùng hash map để đếm số lần xuất hiện của các số đã gặp nhưng chưa ghép
- Với mỗi num:
    + cần tìm số bù là k - num
    + nếu số bù đang có sẵn thì ghép thành 1 cặp, tăng đáp án
    + nếu chưa có thì lưu num lại để chờ ghép sau
- Cách này giúp xử lý trong O(n)

Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List
from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        operations = 0

        for num in nums:
            complement = k - num

            if count[complement] > 0:
                count[complement] -= 1
                operations += 1
            else:
                count[num] += 1

        return operations