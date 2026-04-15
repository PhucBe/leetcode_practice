"""
Problem: 626. Exchange Seats
Link: https://leetcode.com/problems/exchange-seats/
Difficulty: Medium
Topics: Database, SQL

Idea:
- Ta cần đổi chỗ cho từng cặp sinh viên liên tiếp
- Với mỗi dòng:
    + nếu id là lẻ và không phải id cuối cùng -> chuyển sang id + 1
    + nếu id là chẵn -> chuyển sang id - 1
    + nếu là sinh viên cuối cùng khi số lượng sinh viên là lẻ -> giữ nguyên
- Vì id tăng liên tục từ 1 nên id cuối cùng chính là COUNT(*)
- Dùng CASE WHEN để tạo lại id mới sau khi swap
- Sau đó ORDER BY id để kết quả hiển thị đúng thứ tự tăng dần

Time Complexity: O(n)
Space Complexity: O(1)
"""
SELECT
    CASE
        WHEN id % 2 = 1 AND id <> (SELECT COUNT(*) FROM Seat) THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
        ELSE id
    END AS id,
    student
FROM Seat
ORDER BY id;