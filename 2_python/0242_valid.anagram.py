"""
Problem: 0242. Valid Anagram
Link:
Difficulty: Easy
Toppics: Hash Table, String, Sorting

Idea:
- 
- 
- 
- 

Time Complexity: Sorting O(n log n), Hash Map O(n)
Space Complexity: Sorting O(n), Hash Map O(n)

Notes:
-
-
"""

# Cách 1: Sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
# Cách 2: Dùng dictionary/ đếm tần suất
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False

        return True
    
# Cách 3: Dùng Counter
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)