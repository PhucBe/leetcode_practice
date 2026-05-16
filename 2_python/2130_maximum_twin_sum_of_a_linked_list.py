"""
Problem: 2130. Maximum Twin Sum of a Linked List
Link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
Difficulty: Medium
Topics: Linked List, Two Pointers

Idea:
- Twin của node i là node n - 1 - i
- Nghĩa là:
    + node đầu đi với node cuối
    + node thứ 2 đi với node áp cuối
    + ...
- Ta cần tìm twin sum lớn nhất

- Vì linked list không truy cập ngẫu nhiên như mảng, cách tối ưu là:
    + tìm điểm giữa danh sách
    + đảo ngược nửa sau của linked list
    + duyệt song song:
        first từ đầu danh sách
        second từ đầu nửa sau đã đảo
    + mỗi cặp first và second lúc này chính là một cặp twin
    + tính tổng và cập nhật giá trị lớn nhất

- Vì đề cho n luôn chẵn nên sau khi tìm middle:
    + nửa đầu và nửa sau có cùng số node

Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first = head
        second = prev
        max_sum = 0

        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum