"""
Problem: 283. Move Zeroes
Link: https://leetcode.com/problems/move-zeroes/
Difficulty: Easy
Topics: Array, Two Pointers

Idea:
- Dùng một con trỏ `write` để chỉ vị trí tiếp theo cần đặt số khác 0
- Duyệt mảng bằng con trỏ `read`
- Nếu `nums[read] != 0` thì đổi chỗ `nums[read]` với `nums[write]`
- Sau đó tăng `write`
- Kết quả:
    + mọi số khác 0 được đẩy về đầu mảng theo đúng thứ tự ban đầu
    + các số 0 tự động bị dồn về cuối

Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0

        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1