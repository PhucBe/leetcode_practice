"""
Problem: 392. Is Subsequence
Link: https://leetcode.com/problems/is-subsequence/
Difficulty: Easy
Topics: Two Pointers, String

Idea:
- Dùng 2 con trỏ:
    + i trỏ vào chuỗi s
    + j trỏ vào chuỗi t
- Duyệt chuỗi t từ trái sang phải
- Nếu s[i] == t[j] thì tăng i
- Luôn tăng j sau mỗi bước
- Nếu i đi hết chuỗi s, nghĩa là mọi ký tự của s đã xuất hiện đúng thứ tự trong t

Time Complexity: O(len(t))
Space Complexity: O(1)
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)