"""
Problem: 20. Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy
Topics: String, Stack

Idea:
- Dùng stack để lưu các dấu ngoặc mở
- Khi gặp:
    + '(' hoặc '{' hoặc '[':
        -> push vào stack
    + ')' hoặc '}' hoặc ']':
        -> phải kiểm tra:
            1. stack có rỗng không
            2. phần tử trên cùng có khớp loại ngoặc không
- Nếu:
    + stack rỗng khi gặp ngoặc đóng
    + hoặc ngoặc không khớp
  -> chuỗi không hợp lệ
- Sau khi duyệt xong:
    + nếu stack rỗng -> hợp lệ
    + ngược lại -> còn ngoặc mở chưa đóng -> không hợp lệ

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in '({[':
                stack.append(char)

            else:
                if not stack or stack[-1] != mapping[char]:
                    return False

                stack.pop()

        return len(stack) == 0