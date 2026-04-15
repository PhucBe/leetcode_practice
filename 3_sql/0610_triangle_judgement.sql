-- Problem: 610. Triangle Judgement
-- Link: https://leetcode.com/problems/triangle-judgement/
-- Difficulty: Easy
-- Topics: Database, CASE

-- Idea:
-- - Ba cạnh tạo thành tam giác khi tổng hai cạnh bất kỳ lớn hơn cạnh còn lại
-- - Điều kiện tam giác:
--     x + y > z
--     x + z > y
--     y + z > x
-- - Dùng CASE WHEN để trả về 'Yes' hoặc 'No'

SELECT
    x,
    y,
    z,
    CASE
        WHEN x + y > z
         AND x + z > y
         AND y + z > x THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;