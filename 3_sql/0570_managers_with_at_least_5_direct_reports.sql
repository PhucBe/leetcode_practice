-- Problem: 570. Managers with at Least 5 Direct Reports
-- Link: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
-- Difficulty: Medium
-- Topics: Database, Group By, Having, Self Join

-- Idea:
-- - Mỗi nhân viên có managerId trỏ đến id của quản lý
-- - Cần tìm những manager có ít nhất 5 nhân viên báo cáo trực tiếp
-- - Đếm số nhân viên theo managerId
-- - Lọc những manager có COUNT >= 5
-- - Join lại với bảng Employee để lấy tên manager

SELECT
    e1.name
FROM Employee e1
JOIN Employee e2
    ON e1.id = e2.managerId
GROUP BY e1.id, e1.name
HAVING COUNT(e2.id) >= 5;