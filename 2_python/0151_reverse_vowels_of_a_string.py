"""
Problem: 151. Reverse Words in a String
Link: https://leetcode.com/problems/reverse-words-in-a-string/
Difficulty: Medium
Topics: String, Two Pointers

Idea:
- Tách các từ trong chuỗi bằng split()
- split() tự bỏ leading spaces, trailing spaces, và gộp nhiều spaces liên tiếp
- Đảo ngược danh sách các từ
- Nối lại bằng đúng 1 dấu cách

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return " ".join(words)