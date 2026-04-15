"""
Problem: 443. String Compression
Link: https://leetcode.com/problems/string-compression/
Difficulty: Medium
Topics: Array, Two Pointers, String

Idea:
- Duyệt mảng theo từng nhóm ký tự giống nhau liên tiếp
- Với mỗi nhóm:
    + Ghi ký tự đó vào vị trí write
    + Nếu số lần lặp > 1 thì ghi thêm từng chữ số của số đếm
- Dùng 2 con trỏ:
    + read để duyệt mảng gốc
    + write để ghi đè kết quả nén ngay trên mảng chars
- Vì ghi trực tiếp trên mảng đầu vào nên chỉ dùng O(1) extra space

Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        write = 0
        read = 0

        while read < n:
            current_char = chars[read]
            count = 0

            while read < n and chars[read] == current_char:
                read += 1
                count += 1

            chars[write] = current_char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write