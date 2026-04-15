"""
Problem: 1071. Greatest Common Divisor of Strings
Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/
Difficulty: Easy
Topics: String, Math

Idea:
- Nếu hai chuỗi có cùng chuỗi gốc lặp lại, thì str1 + str2 phải bằng str2 + str1
- Nếu không bằng nhau thì không có đáp án
- Nếu bằng nhau, đáp án có độ dài bằng gcd(len(str1), len(str2))

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""

from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        length = gcd(len(str1), len(str2))
        return str1[:length]