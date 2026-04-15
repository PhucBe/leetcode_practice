"""
Problem: 649. Dota2 Senate
Link: https://leetcode.com/problems/dota2-senate/
Difficulty: Medium
Topics: String, Queue, Greedy, Simulation

Idea:
- Mỗi senator sẽ cố gắng loại một senator của phe đối lập để phe mình sống lâu nhất
- Ta dùng 2 queue:
    + queue_R lưu vị trí của các senator Radiant
    + queue_D lưu vị trí của các senator Dire
- Vì lượt hành động diễn ra theo thứ tự từ trái sang phải, nên vị trí nhỏ hơn sẽ được hành động trước
- Ở mỗi bước:
    + lấy senator đầu tiên của mỗi phe ra so sánh vị trí
    + ai có vị trí nhỏ hơn thì người đó được hành động trước và ban người kia
    + người thắng sẽ quay lại vòng sau với vị trí mới là index + n
- Tại sao cộng thêm n:
    + vì sau khi đi hết một vòng, senator còn sống sẽ tiếp tục tham gia ở vòng tiếp theo
    + index + n giúp mô phỏng việc quay lại cuối hàng
- Khi một trong hai queue rỗng, phe còn lại thắng

Time Complexity: O(n)
Space Complexity: O(n)
"""
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()

        for i, ch in enumerate(senate):
            if ch == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r_index = radiant.popleft()
            d_index = dire.popleft()

            if r_index < d_index:
                radiant.append(r_index + n)
            else:
                dire.append(d_index + n)

        return "Radiant" if radiant else "Dire"