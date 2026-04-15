-- Problem: 0177. Nth Highest Salary
-- Link: https://leetcode.com/problems/nth-highest-salary/
-- Difficulty: Medium
-- Topic: SQL, Function, Subquery
--
-- Idea:
-- 1. Lấy các mức lương distinct
-- 2. Sắp xếp giảm dần
-- 3. Dùng OFFSET = N - 1 để lấy mức lương cao thứ N
-- 4. Nếu không đủ N mức lương thì RETURN NULL
--
-- Notes:
-- - DISTINCT rất quan trọng vì đề yêu cầu nth highest distinct salary
-- - OFFSET bắt đầu từ 0 nên cần N = N - 1
-- - Nếu query không trả về dòng nào thì kết quả là NULL

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  
  RETURN (
      SELECT DISTINCT salary
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET N
  );
END