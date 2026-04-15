"""
Problem: 0049. Group Anagrams
Link: 
Difficulty: Medium
Toppics: Array, String, Hash Map, Sorting

Idea:
- 
- 
- 
- 

Time Complexity: O(n*k*log(k))
Space Complexity: O(n*k)

Notes:
-
-
"""
from typing import List
from collections import defaultdict

# Cách 1
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)

        return list(groups.values())

# Cách 2
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1

            groups[tuple(count)].append(s)

        return list(groups.values())