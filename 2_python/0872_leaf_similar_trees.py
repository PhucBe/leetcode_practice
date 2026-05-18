"""
Problem: 872. Leaf-Similar Trees
Link: https://leetcode.com/problems/leaf-similar-trees/
Difficulty: Easy
Topics: Tree, Depth-First Search, Binary Tree

Idea:
- Hai cây được gọi là leaf-similar nếu dãy giá trị các lá từ trái sang phải giống hệt nhau
- Vì vậy bài toán trở thành:
    + lấy ra dãy lá của cây thứ nhất
    + lấy ra dãy lá của cây thứ hai
    + so sánh hai dãy này
- Dùng DFS để duyệt cây:
    + nếu node là lá (không có left và right) -> thêm giá trị vào list
    + ngược lại -> tiếp tục duyệt trái rồi phải
- Duyệt trái trước, phải sau để đảm bảo đúng thứ tự từ trái sang phải

Time Complexity: O(n + m)
Space Complexity: O(n + m)
- n là số node của cây 1
- m là số node của cây 2
"""
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(node: Optional[TreeNode], leaves: List[int]) -> None:
            if not node:
                return

            if not node.left and not node.right:
                leaves.append(node.val)
                return

            get_leaves(node.left, leaves)
            get_leaves(node.right, leaves)

        leaves1 = []
        leaves2 = []

        get_leaves(root1, leaves1)
        get_leaves(root2, leaves2)

        return leaves1 == leaves2