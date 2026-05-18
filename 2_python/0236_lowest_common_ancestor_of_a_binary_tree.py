"""
Problem: 236. Lowest Common Ancestor of a Binary Tree
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
Difficulty: Medium
Topics: Tree, Depth-First Search, Binary Tree, Recursion

Idea:
- Ta cần tìm node thấp nhất trong cây sao cho:
    + node đó có p là hậu duệ
    + node đó có q là hậu duệ
- "Thấp nhất" nghĩa là gần p và q nhất từ phía dưới đi lên

- Dùng DFS đệ quy:
    + nếu root là None -> trả về None
    + nếu root chính là p hoặc q -> trả về root
- Sau đó đệ quy xuống trái và phải:
    + left = LCA ở cây con trái
    + right = LCA ở cây con phải

- Có 3 trường hợp:
    + nếu left và right đều khác None:
        -> p và q nằm ở 2 phía khác nhau
        -> root hiện tại chính là LCA
    + nếu chỉ một bên khác None:
        -> cả p và q đều nằm trong một phía, hoặc root là một trong hai node
        -> trả về bên khác None đó
    + nếu cả hai đều None:
        -> không tìm thấy p, q trong cây con này
        -> trả về None

Time Complexity: O(n)
Space Complexity: O(h)
- h là chiều cao cây
- worst case: O(n) nếu cây lệch
- balanced tree: O(log n)
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode'
    ) -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right