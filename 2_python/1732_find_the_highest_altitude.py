"""
Problem: 1732. Find the Highest Altitude
Link: https://leetcode.com/problems/find-the-highest-altitude/
Difficulty: Easy
Topics: Array, Prefix Sum

Idea:
- Bắt đầu từ độ cao 0
- Duyệt mảng gain, cộng dồn để tính độ cao hiện tại sau mỗi chặng
- Trong lúc cộng dồn, cập nhật độ cao lớn nhất đã đạt được
- Kết quả là giá trị lớn nhất giữa các độ cao trên hành trình

Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        highest_altitude = 0

        for g in gain:
            current_altitude += g
            highest_altitude = max(highest_altitude, current_altitude)

        return highest_altitude