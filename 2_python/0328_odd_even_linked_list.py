"""
Problem: 328. Odd Even Linked List
Link: https://leetcode.com/problems/odd-even-linked-list/
Difficulty: Medium
Topics: Linked List

Idea:
- Bài này không tách theo giá trị lẻ/chẵn
- Mà tách theo vị trí:
    + node thứ 1, 3, 5, ... là odd
    + node thứ 2, 4, 6, ... là even
- Ta cần:
    + gom toàn bộ node odd lại trước
    + sau đó nối với danh sách even
    + vẫn giữ nguyên thứ tự tương đối trong từng nhóm

- Dùng 3 con trỏ:
    + odd: chạy trên dãy odd
    + even: chạy trên dãy even
    + even_head: lưu đầu của dãy even để cuối cùng nối lại

- Ý tưởng chính:
    + odd.next = even.next
      -> bỏ qua node even hiện tại để nối odd với odd tiếp theo
    + odd = odd.next
    + even.next = odd.next
      -> bỏ qua node odd mới để nối even với even tiếp theo
    + even = even.next

- Khi duyệt xong:
    + dãy odd đã được nối lại với nhau
    + dãy even đã được nối lại với nhau
    + chỉ cần odd.next = even_head

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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head