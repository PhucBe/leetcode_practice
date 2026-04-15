"""
Problem: 627. Swap Salary
Link: https://leetcode.com/problems/swap-salary/
Difficulty: Easy
Topics: Database, SQL

Idea:
- Đề bài yêu cầu:
    + đổi toàn bộ 'm' thành 'f'
    + đổi toàn bộ 'f' thành 'm'
    + chỉ dùng đúng 1 câu lệnh UPDATE
    + không dùng bảng tạm
- Dùng CASE WHEN ngay trong UPDATE:
    + nếu sex = 'm' thì đổi thành 'f'
    + ngược lại đổi thành 'm'
- Vì cột sex chỉ có 2 giá trị là 'm' và 'f', nên chỉ cần CASE đơn giản là đủ

Time Complexity: O(n)
Space Complexity: O(1)
"""
UPDATE Salary
SET sex = CASE
    WHEN sex = 'm' THEN 'f'
    ELSE 'm'
END;