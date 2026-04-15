"""
Problem: 1768. Merge Strings Alternately
Link: https://leetcode.com/problems/merge-strings-alternately/
Difficulty: Easy
Topics: Two Pointers, String

Idea:
- Duyệt 2 chuỗi cùng lúc
- Mỗi lần lấy 1 ký tự từ word1 rồi 1 ký tự từ word2
- Nếu một chuỗi còn dư thì nối phần còn lại vào cuối

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

        for i in range(min(len(word1), len(word2))):
            result.append(word1[i])
            result.append(word2[i])

        result.append(word1[len(word2):])
        result.append(word2[len(word1):])

        return "".join(result)