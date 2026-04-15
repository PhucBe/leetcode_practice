"""
Problem: 1431. Kids With the Greatest Number of Candies
Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
Difficulty: Easy
Topics: Array

Idea:
- Tìm số kẹo lớn nhất hiện tại
- Với mỗi bạn, kiểm tra nếu cho thêm extraCandies thì có đạt hoặc vượt mức lớn nhất không
- Nếu có thì True, ngược lại False

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        result = []

        for candy in candies:
            result.append(candy + extraCandies >= max_candies)

        return result