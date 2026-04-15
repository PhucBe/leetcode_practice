-- Problem: 0185. Department Top Three Salaries
-- Link: https://leetcode.com/problems/department-top-three-salaries/
-- Difficulty: Hard
-- Topic: SQL, Window Function, DENSE_RANK
--
-- Idea:
-- - Xếp hạng mức lương trong từng department bằng DENSE_RANK()
-- - DENSE_RANK() giúp các mức lương bằng nhau có cùng hạng
-- - Không bị nhảy số giữa các mức lương phân biệt
-- - Lọc các nhân viên có rank <= 3
--
-- Notes:
-- - Đề yêu cầu top three unique salaries, không phải top 3 employees
-- - Không dùng ROW_NUMBER() vì sẽ loại mất người cùng mức lương
-- - Không dùng RANK() vì sẽ bị nhảy hạng sau tie

SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM (
    SELECT
        name,
        salary,
        departmentId,
        DENSE_RANK() OVER (
            PARTITION BY departmentId
            ORDER BY salary DESC
        ) AS salary_rank
    FROM Employee
) e
JOIN Department d
    ON e.departmentId = d.id
WHERE e.salary_rank <= 3;