"""
Problem: 1456. Maximum Number of Vowels in a Substring of Given Length
Link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
Difficulty: Medium
Topics: String, Sliding Window

Idea:
- Ta cần tìm substring liên tiếp có độ dài đúng bằng k và chứa nhiều nguyên âm nhất
- Dùng sliding window độ dài cố định k
- Đếm số nguyên âm trong cửa sổ đầu tiên
- Sau đó trượt cửa sổ sang phải:
    + nếu ký tự mới thêm vào là nguyên âm thì tăng count
    + nếu ký tự bị loại ra là nguyên âm thì giảm count
- Cập nhật kết quả lớn nhất trong quá trình trượt

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        current_count = 0

        for i in range(k):
            if s[i] in vowels:
                current_count += 1

        max_count = current_count

        for i in range(k, len(s)):
            if s[i] in vowels:
                current_count += 1
            if s[i - k] in vowels:
                current_count -= 1

            max_count = max(max_count, current_count)

        return max_count