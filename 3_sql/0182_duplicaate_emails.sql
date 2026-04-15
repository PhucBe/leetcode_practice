-- Problem: 0182. Duplicate Emails
-- Link: https://leetcode.com/problems/duplicate-emails/
-- Difficulty: Easy
-- Topic: SQL, GROUP BY, HAVING
--
-- Idea:
-- - Gom các dòng theo email
-- - Đếm số lần xuất hiện của mỗi email
-- - Giữ lại những email xuất hiện hơn 1 lần
--
-- Notes:
-- - GROUP BY dùng để gom các email giống nhau
-- - HAVING dùng để lọc sau khi đã group
-- - COUNT(*) > 1 nghĩa là email bị trùng

SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;