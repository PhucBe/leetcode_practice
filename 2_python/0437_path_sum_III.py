"""
Problem: 437. Path Sum III
Link: https://leetcode.com/problems/path-sum-iii/
Difficulty: Medium
Topics: Tree, Depth-First Search, Binary Tree, Hash Table, Prefix Sum

Idea:
- Ta cần đếm số đường đi có tổng bằng targetSum
- Đường đi:
    + chỉ được đi từ trên xuống dưới
    + không bắt buộc bắt đầu từ root
    + không bắt buộc kết thúc ở leaf
- Đây là điểm khó nhất của bài

- Dùng Prefix Sum trên cây:
    + current_sum = tổng từ root tới node hiện tại
    + nếu tồn tại một prefix_sum trước đó sao cho:
        current_sum - prefix_sum = targetSum
      thì đoạn path từ sau prefix_sum đó tới node hiện tại có tổng bằng targetSum

- Suy ra:
    số path kết thúc tại node hiện tại có tổng = targetSum
    chính là số lần xuất hiện của:
        current_sum - targetSum
    trong hash map prefix_count

- prefix_count[x] = đã có bao nhiêu lần prefix sum = x trên đường đi hiện tại từ root xuống node cha
- Khởi tạo:
    prefix_count[0] = 1
  để xử lý trường hợp path bắt đầu ngay từ root

- DFS xuống cây:
    1. cập nhật current_sum
    2. cộng vào đáp án số lần xuất hiện của (current_sum - targetSum)
    3. thêm current_sum vào hash map
    4. DFS trái và phải
    5. backtrack: giảm current_sum ra khỏi hash map khi quay lui

Time Complexity: O(n)
Space Complexity: O(h)
- h là chiều cao cây cho recursion stack
- hash map trên một path xấu nhất có thể là O(n)
"""
from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        def dfs(node: Optional[TreeNode], current_sum: int) -> int:
            if not node:
                return 0

            current_sum += node.val

            path_count = prefix_count[current_sum - targetSum]

            prefix_count[current_sum] += 1

            path_count += dfs(node.left, current_sum)
            path_count += dfs(node.right, current_sum)

            prefix_count[current_sum] -= 1

            return path_count

        return dfs(root, 0)