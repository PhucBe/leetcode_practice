"""
Problem: 1004. Max Consecutive Ones III
Link: https://leetcode.com/problems/max-consecutive-ones-iii/
Difficulty: Medium
Topics: Array, Sliding Window

Idea:
- Ta cần tìm đoạn con dài nhất sao cho trong đoạn đó có nhiều nhất k số 0
- Vì ta được phép lật tối đa k số 0 thành 1, nên một cửa sổ hợp lệ là cửa sổ có:
    số lượng số 0 <= k
- Dùng sliding window:
    + mở rộng right để duyệt mảng
    + đếm số 0 trong cửa sổ hiện tại
    + nếu số 0 > k thì thu hẹp cửa sổ từ bên trái
- Mỗi khi cửa sổ hợp lệ, cập nhật độ dài lớn nhất

Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length