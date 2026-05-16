"""
Problem: 206. Reverse Linked List
Link: https://leetcode.com/problems/reverse-linked-list/
Difficulty: Easy
Topics: Linked List, Recursion

Idea:
- Ta cần đảo ngược toàn bộ linked list
- Ví dụ:
    1 -> 2 -> 3 -> 4 -> 5
  thành:
    5 -> 4 -> 3 -> 2 -> 1

- Cách tối ưu nhất là duyệt từng node và đảo chiều con trỏ next
- Dùng 3 con trỏ:
    + prev: node đứng trước, ban đầu là None
    + curr: node hiện tại đang xử lý
    + nxt: lưu node tiếp theo để không bị mất danh sách

- Ở mỗi bước:
    + lưu curr.next vào nxt
    + đảo chiều: curr.next = prev
    + cho prev tiến lên curr
    + cho curr tiến lên nxt

- Khi curr đi hết danh sách:
    + prev sẽ đứng ở đầu danh sách mới đã đảo

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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev