-- Problem: 619. Biggest Single Number
-- Link: https://leetcode.com/problems/biggest-single-number/
-- Difficulty: Easy
-- Topics: Database, Group By, Having, Aggregate

-- Idea:
-- - Single number là số xuất hiện đúng 1 lần
-- - Gom nhóm theo num
-- - Chỉ giữ những num có COUNT(*) = 1
-- - Trong các số đó, lấy số lớn nhất bằng MAX(num)
-- - Nếu không có số nào thỏa thì MAX(...) sẽ trả về NULL

SELECT
    MAX(num) AS num
FROM (
    SELECT
        num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) t;