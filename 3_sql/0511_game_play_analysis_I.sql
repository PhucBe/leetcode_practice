-- Problem: 511. Game Play Analysis I
-- Link: https://leetcode.com/problems/game-play-analysis-i/
-- Difficulty: Easy
-- Topics: Database, Aggregation, Group By

-- Idea:
-- - Với mỗi player_id, cần tìm ngày đăng nhập đầu tiên
-- - Ngày đầu tiên chính là giá trị nhỏ nhất của event_date
-- - Dùng GROUP BY theo player_id
-- - Dùng MIN(event_date) để lấy first login date

SELECT
    player_id,
    MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;