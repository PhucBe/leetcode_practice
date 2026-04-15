"""
Problem: 605. Can Place Flowers
Link: https://leetcode.com/problems/can-place-flowers/
Difficulty: Easy
Topics: Array, Greedy

Idea:
- Duyệt từng vị trí
- Nếu ô hiện tại trống và hai ô bên cạnh cũng trống thì trồng tại đó
- Cập nhật flowerbed ngay sau khi trồng
- Đếm số hoa đã trồng được và so với n

Time Complexity: O(m)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
            
        testFlowerbed = [0] + flowerbed + [0]

        for i in range(1, len(testFlowerbed) - 1):
            if (testFlowerbed[i-1] == 0) and (testFlowerbed[i] == 0) and (testFlowerbed[i+1] == 0):
                testFlowerbed[i] = 1
                n -= 1
            if n == 0:
                return True

        return False