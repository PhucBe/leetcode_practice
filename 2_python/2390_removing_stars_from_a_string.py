"""
Problem: 2390. Removing Stars From a String
Link: https://leetcode.com/problems/removing-stars-from-a-string/
Difficulty: Medium
Topics: String, Stack, Simulation

Idea:
- Mỗi khi gặp ký tự thường, ta giữ lại nó
- Mỗi khi gặp dấu '*', ta phải xóa ký tự gần nhất bên trái chưa bị xóa
- Cách tự nhiên nhất là dùng stack:
    + gặp chữ cái -> push vào stack
    + gặp '*' -> pop phần tử trên cùng ra khỏi stack
- Vì ký tự trên cùng của stack chính là ký tự gần nhất bên trái còn tồn tại
- Sau khi duyệt xong, nối các ký tự trong stack lại thành kết quả

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == '*':
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)