-- Problem: 0181. Employees Earning More Than Their Managers
-- Link: https://leetcode.com/problems/employees-earning-more-than-their-managers/
-- Difficulty: Easy
-- Topic: SQL, Self Join
--
-- Idea:
-- - Bảng Employee chứa cả nhân viên và manager
-- - Dùng self join để nối mỗi nhân viên với manager của họ
-- - So sánh salary của nhân viên với salary của manager
--
-- Notes:
-- - e = employee
-- - m = manager
-- - Chỉ cần INNER JOIN vì chỉ những ai có manager mới cần xét

SELECT e.name AS Employee
FROM Employee e
JOIN Employee m
    ON e.managerId = m.id
WHERE e.salary > m.salary;