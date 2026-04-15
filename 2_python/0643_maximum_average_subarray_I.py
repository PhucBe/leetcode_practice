"""
Problem: 643. Maximum Average Subarray I
Link: https://leetcode.com/problems/maximum-average-subarray-i/
Difficulty: Easy
Topics: Array, Sliding Window

Idea:
- Ta cần tìm subarray liên tiếp có độ dài đúng bằng k và có average lớn nhất
- Vì average = sum / k, nên chỉ cần tìm subarray có tổng lớn nhất
- Dùng sliding window:
    + Tính tổng của cửa sổ đầu tiên độ dài k
    + Sau đó trượt cửa sổ sang phải từng bước:
        tổng mới = tổng cũ - phần tử rời cửa sổ + phần tử mới vào cửa sổ
    + Cập nhật tổng lớn nhất
- Cuối cùng trả về max_sum / k

Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k