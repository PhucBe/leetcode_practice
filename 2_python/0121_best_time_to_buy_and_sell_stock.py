"""
Problem: 0121. Best Time To Buy And Sell Stock
Link: 
Difficulty: Easy
Toppics: Array, Dynamic Programming

Idea:
- 
- 
- 
- 

Time Complexity: O(n)
Space Complexity: O(1)

Notes:
-
-
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit