-- Problem: 0176. Second Highest Salary
-- Link: https://leetcode.com/problems/second-highest-salary/
-- Difficulty: Medium
-- Topic: SQL, Subquery
--
-- Idea:
-- 1. Lấy các mức lương distinct
-- 2. Sắp xếp giảm dần
-- 3. Bỏ qua mức lương cao nhất
-- 4. Lấy mức lương tiếp theo

-- Cách 1: DISTINCT + ORDER BY + LIMIT OFFSET
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;

-- Cách 2: MAX + Subquery
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (
    SELECT MAX(salary)
    FROM Employee
);