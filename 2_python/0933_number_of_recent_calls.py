"""
Problem: 933. Number of Recent Calls
Link: https://leetcode.com/problems/number-of-recent-calls/
Difficulty: Easy
Topics: Queue, Design, Data Stream

Idea:
- Mỗi lần ping(t), ta cần đếm bao nhiêu request nằm trong đoạn:
    [t - 3000, t]
- Vì các giá trị t luôn tăng dần, nên các request cũ hơn sẽ không bao giờ cần dùng lại
- Dùng queue để lưu các thời điểm request còn hợp lệ:
    + thêm t mới vào queue
    + loại bỏ ở đầu queue những thời điểm < t - 3000
- Sau khi xóa xong, toàn bộ phần tử còn lại trong queue chính là các request nằm trong khoảng yêu cầu
- Kết quả mỗi lần ping là độ dài của queue

Time Complexity: O(1) amortized cho mỗi lần ping
Space Complexity: O(n)
"""
from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)

        while self.q[0] < t - 3000:
            self.q.popleft()

        return len(self.q)