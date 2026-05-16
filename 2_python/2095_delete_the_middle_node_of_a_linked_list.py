"""
Problem: 2095. Delete the Middle Node of a Linked List
Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
Difficulty: Medium
Topics: Linked List, Two Pointers

Idea:
- Ta cần xóa node ở vị trí giữa của linked list
- Vị trí giữa được tính là: floor(n / 2) theo chỉ số 0-based
- Cách tối ưu là dùng slow pointer và fast pointer:
    + slow đi 1 bước
    + fast đi 2 bước
- Khi fast đi tới cuối danh sách:
    + slow sẽ đứng ở node giữa
- Nhưng để xóa node giữa, ta cần node đứng trước nó
- Vì vậy dùng thêm prev để lưu node trước slow
- Các bước:
    + nếu list chỉ có 1 node, xóa node đó thì kết quả là None
    + dùng slow, fast để tìm middle
    + prev.next = slow.next để bỏ qua node giữa

Time Complexity: O(n)
Space Complexity: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head