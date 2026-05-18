"""
Problem: 1448. Count Good Nodes in Binary Tree
Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
Difficulty: Medium
Topics: Tree, Depth-First Search, Binary Tree, Recursion

Idea:
- Một node được gọi là good nếu trên đường đi từ root tới node đó
  không có node nào có giá trị lớn hơn nó
- Nói cách khác:
    + node hiện tại là good nếu node.val >= max_value_trên_đường_đi
- Khi DFS xuống cây, ta chỉ cần mang theo:
    + giá trị lớn nhất đã gặp từ root tới node hiện tại
- Với mỗi node:
    + nếu node.val >= max_so_far -> node này là good
    + cập nhật max_so_far mới = max(max_so_far, node.val)
    + tiếp tục DFS sang trái và phải
- Kết quả là:
    số good ở node hiện tại
    + số good ở cây con trái
    + số good ở cây con phải

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
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], max_so_far: int) -> int:
            if not node:
                return 0

            good = 1 if node.val >= max_so_far else 0
            max_so_far = max(max_so_far, node.val)

            left_good = dfs(node.left, max_so_far)
            right_good = dfs(node.right, max_so_far)

            return good + left_good + right_good

        return dfs(root, root.val)