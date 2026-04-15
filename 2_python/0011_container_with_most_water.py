"""
Problem: 11. Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/
Difficulty: Medium
Topics: Array, Two Pointers, Greedy

Idea:
- Dùng 2 con trỏ:
    + left ở đầu mảng
    + right ở cuối mảng
- Diện tích tạo bởi 2 cột:
    area = min(height[left], height[right]) * (right - left)
- Mỗi bước cập nhật diện tích lớn nhất
- Sau đó di chuyển con trỏ ở phía có chiều cao nhỏ hơn:
    + vì chiều cao bị giới hạn bởi cạnh thấp hơn
    + nếu giữ cạnh thấp hơn thì dù khoảng cách giảm, diện tích khó tăng
- Nếu hai cạnh bằng nhau thì di chuyển một trong hai đều được

Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area