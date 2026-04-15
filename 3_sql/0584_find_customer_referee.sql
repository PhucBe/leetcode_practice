-- Problem: 584. Find Customer Referee
-- Link: https://leetcode.com/problems/find-customer-referee/
-- Difficulty: Easy
-- Topics: Database, Filter, NULL

-- Idea:
-- - Cần lấy những customer:
--     + không bị giới thiệu bởi ai (referee_id IS NULL)
--     + hoặc được giới thiệu bởi người có id khác 2
-- - Loại những customer có referee_id = 2
-- - Chú ý trong SQL, NULL phải kiểm tra bằng IS NULL, không dùng = NULL

SELECT
    name
FROM Customer
WHERE referee_id != 2
   OR referee_id IS NULL;