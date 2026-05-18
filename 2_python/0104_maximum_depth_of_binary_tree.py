"""
Problem: 104. Maximum Depth of Binary Tree
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Difficulty: Easy
Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree, Recursion

Idea:
- Độ sâu lớn nhất của cây là số node trên đường đi dài nhất từ root tới leaf xa nhất
- Với mỗi node:
    + độ sâu của cây con trái = maxDepth(node.left)
    + độ sâu của cây con phải = maxDepth(node.right)
    + độ sâu tại node hiện tại = 1 + max(trái, phải)
- Đây là bài toán đệ quy rất tự nhiên:
    + nếu node là None -> độ sâu = 0
    + ngược lại -> lấy độ sâu lớn hơn giữa trái và phải, rồi cộng thêm 1 cho node hiện tại

Time Complexity: O(n)
Space Complexity: O(h), với h là chiều cao cây
- Trường hợp xấu nhất: O(n) nếu cây bị lệch hoàn toàn
- Trường hợp cân bằng: O(log n)
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)