"""
Problem: 0003. Longest Substring Without Repeating Characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Difficulty: Medium
Toppics: String, Hash Table, Sliding Window

Idea:
- 
- 
- 
- 

Time Complexity: O(n)
Space Complexity: O(n)

Notes:
-
-
"""

# Using Set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

# Using Dictionary
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_len = 0

        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1

            last_seen[ch] = right
            max_len = max(max_len, right - left + 1)

        return max_len