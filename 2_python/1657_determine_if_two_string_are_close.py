"""
Problem: 1657. Determine if Two Strings Are Close
Link: https://leetcode.com/problems/determine-if-two-strings-are-close/
Difficulty: Medium
Topics: Hash Table, String, Sorting, Counting

Idea:
- Hai chuỗi close phải có cùng độ dài
- Hai chuỗi phải có cùng tập ký tự
    + Vì Operation 2 chỉ được biến đổi giữa các ký tự đã tồn tại sẵn trong chuỗi
    + Không thể tự tạo ra một ký tự mới chưa từng xuất hiện
- Tần suất xuất hiện không cần gắn đúng ký tự ban đầu, nhưng multiset frequency phải giống nhau
    + Vì Operation 1 chỉ đổi vị trí
    + Vì Operation 2 cho phép hoán đổi vai trò giữa các ký tự đã tồn tại
- Do đó chỉ cần kiểm tra:
    1. set(word1) == set(word2)
    2. sorted(count(word1).values()) == sorted(count(word2).values())

Time Complexity: O(n log n)
Space Complexity: O(1)
"""
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        count1 = Counter(word1)
        count2 = Counter(word2)

        if set(count1.keys()) != set(count2.keys()):
            return False

        return sorted(count1.values()) == sorted(count2.values())