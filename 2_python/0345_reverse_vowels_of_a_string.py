"""
Problem: 345. Reverse Vowels of a String
Link: https://leetcode.com/problems/reverse-vowels-of-a-string/
Difficulty: Easy
Topics: Two Pointers, String

Idea:
- Dùng hai con trỏ: một ở đầu chuỗi, một ở cuối chuỗi
- Di chuyển con trỏ trái cho đến khi gặp nguyên âm
- Di chuyển con trỏ phải cho đến khi gặp nguyên âm
- Khi cả hai đều đang trỏ vào nguyên âm thì hoán đổi
- Tiếp tục cho đến khi hai con trỏ gặp nhau

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)

        left, right = 0, len(chars) - 1

        while left < right:
            while left < right and chars[left] not in vowels:
                left += 1

            while left < right and chars[right] not in vowels:
                right -= 1

            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

        return "".join(chars)