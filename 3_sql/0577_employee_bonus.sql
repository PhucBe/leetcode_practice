-- Problem: 577. Employee Bonus
-- Link: https://leetcode.com/problems/employee-bonus/
-- Difficulty: Easy
-- Topics: Database, Join, Filter

-- Idea:
-- - Cần lấy tất cả nhân viên, kể cả người không có bonus
-- - Vì vậy dùng LEFT JOIN từ Employee sang Bonus
-- - Sau đó lọc những người:
--     + bonus < 1000
--     + hoặc bonus là NULL (không có thưởng)

SELECT
    e.name,
    b.bonus
FROM Employee e
LEFT JOIN Bonus b
    ON e.empId = b.empId
WHERE b.bonus < 1000
   OR b.bonus IS NULL;