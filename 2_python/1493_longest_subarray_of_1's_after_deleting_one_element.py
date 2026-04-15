"""
Problem: 1493. Longest Subarray of 1's After Deleting One Element
Link: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
Difficulty: Medium
Topics: Array, Sliding Window

Idea:
- Ta phải xóa đúng 1 phần tử
- Bài toán tương đương với việc tìm subarray dài nhất chứa nhiều nhất 1 số 0
- Vì:
    + nếu trong cửa sổ có 1 số 0, ta xóa số 0 đó thì phần còn lại toàn 1
    + nếu trong cửa sổ toàn 1, ta vẫn phải xóa 1 phần tử, nên độ dài kết quả là window_length - 1
- Dùng sliding window:
    + mở rộng right
    + đếm số 0 trong cửa sổ
    + nếu số 0 > 1 thì co cửa sổ từ trái
- Mỗi lúc cửa sổ hợp lệ, cập nhật đáp án bằng:
    right - left
  (không phải right - left + 1, vì ta phải xóa 1 phần tử)

Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_length = max(max_length, right - left)

        return max_length