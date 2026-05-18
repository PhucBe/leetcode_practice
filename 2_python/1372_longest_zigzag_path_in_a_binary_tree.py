"""
Problem: 1372. Longest ZigZag Path in a Binary Tree
Link: https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
Difficulty: Medium
Topics: Tree, Depth-First Search, Dynamic Programming, Binary Tree

Idea:
- ZigZag path nghĩa là mỗi bước phải đổi hướng:
    + nếu vừa đi sang trái thì bước tiếp theo phải đi sang phải
    + nếu vừa đi sang phải thì bước tiếp theo phải đi sang trái
- Ta cần tìm độ dài ZigZag lớn nhất trong toàn bộ cây
- Với mỗi node, ta quan tâm 2 giá trị:
    + left_len:
        độ dài ZigZag dài nhất bắt đầu từ node này nếu bước đầu tiên đi sang trái
    + right_len:
        độ dài ZigZag dài nhất bắt đầu từ node này nếu bước đầu tiên đi sang phải
- Khi đó:
    + nếu đi trái trước:
        left_len = 1 + right_len của node.left
    + nếu đi phải trước:
        right_len = 1 + left_len của node.right
- Dùng DFS hậu tự để lấy kết quả từ con rồi tính cho cha
- Với node rỗng, trả về (-1, -1) để:
    + node lá có left_len = 0
    + node lá có right_len = 0
  đúng với định nghĩa: một node đơn lẻ có độ dài ZigZag = 0

Time Complexity: O(n)
Space Complexity: O(h)
- h là chiều cao cây
- worst case: O(n) nếu cây lệch
- balanced tree: O(log n)
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            if not node:
                return -1, -1

            left_child = dfs(node.left)
            right_child = dfs(node.right)

            left_len = left_child[1] + 1
            right_len = right_child[0] + 1

            self.ans = max(self.ans, left_len, right_len)

            return left_len, right_len

        dfs(root)
        return self.ans