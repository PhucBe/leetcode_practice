"""
Problem: 394. Decode String
Link: https://leetcode.com/problems/decode-string/
Difficulty: Medium
Topics: String, Stack, Recursion

Idea:
- Chuỗi có dạng mã hóa k[encoded_string], nghĩa là phần trong ngoặc được lặp lại k lần
- Ta cần giải mã cả trường hợp lồng nhau, ví dụ: 3[a2[c]]
- Dùng stack để lưu trạng thái khi gặp '[':
    + số lần lặp hiện tại
    + chuỗi đã xây dựng trước đó
- Cách làm:
    + gặp chữ số -> xây dựng số repeat nhiều chữ số
    + gặp '[' -> đẩy (current_string, repeat) vào stack, rồi reset để xử lý phần bên trong ngoặc
    + gặp chữ cái -> nối vào current_string
    + gặp ']' -> lấy trạng thái trước đó từ stack ra, ghép:
        previous_string + current_string * repeat
- Nhờ vậy ta xử lý được cả ngoặc lồng nhau một cách tự nhiên

Time Complexity: O(n + m)
Space Complexity: O(m)
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_string = ""

        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)
            elif ch == "[":
                stack.append((current_string, current_num))
                current_string = ""
                current_num = 0
            elif ch == "]":
                prev_string, repeat = stack.pop()
                current_string = prev_string + current_string * repeat
            else:
                current_string += ch

        return current_string