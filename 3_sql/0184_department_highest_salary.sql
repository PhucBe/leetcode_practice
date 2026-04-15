-- Problem: 0184. Department Highest Salary
-- Link: https://leetcode.com/problems/department-highest-salary/
-- Difficulty: Medium
-- Topic: SQL, GROUP BY, JOIN
--
-- Idea:
-- - Tìm mức lương cao nhất của mỗi department bằng GROUP BY + MAX
-- - Join lại với bảng Employee để lấy những nhân viên có salary bằng mức max đó
-- - Join với Department để lấy tên phòng ban
--
-- Notes:
-- - Nếu nhiều nhân viên cùng mức lương cao nhất trong một department thì phải lấy tất cả
-- - Đây là pattern "top value per group"

SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
JOIN Department d
    ON e.departmentId = d.id
JOIN (
    SELECT departmentId, MAX(salary) AS max_salary
    FROM Employee
    GROUP BY departmentId
) m
    ON e.departmentId = m.departmentId
   AND e.salary = m.max_salary;

-- Sử dụng Window Function
SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM (
    SELECT *,
           DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rnk
    FROM Employee
) e
JOIN Department d
    ON e.departmentId = d.id
WHERE e.rnk = 1;