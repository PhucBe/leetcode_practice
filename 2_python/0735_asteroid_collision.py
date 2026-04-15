"""
Problem: 735. Asteroid Collision
Link: https://leetcode.com/problems/asteroid-collision/
Difficulty: Medium
Topics: Array, Stack, Simulation

Idea:
- Va chạm chỉ xảy ra khi:
    + asteroid bên trái đang đi sang phải  (> 0)
    + asteroid hiện tại đang đi sang trái (< 0)
- Vì vậy ta dùng stack để mô phỏng các asteroid còn sống
- Với mỗi asteroid:
    + nếu không thể va chạm, đưa luôn vào stack
    + nếu có thể va chạm với top của stack, so sánh kích thước:
        - top nhỏ hơn -> top nổ, tiếp tục xét tiếp
        - bằng nhau -> cả hai nổ, dừng
        - top lớn hơn -> asteroid hiện tại nổ, dừng
- Lý do dùng stack:
    + asteroid mới chỉ có thể va chạm với asteroid sống gần nhất bên trái
    + đó chính là phần tử trên cùng của stack

Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            alive = True

            while alive and asteroid < 0 and stack and stack[-1] > 0:
                if stack[-1] < -asteroid:
                    stack.pop()
                elif stack[-1] == -asteroid:
                    stack.pop()
                    alive = False
                else:
                    alive = False

            if alive:
                stack.append(asteroid)

        return stack