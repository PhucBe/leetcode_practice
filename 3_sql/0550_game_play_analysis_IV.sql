-- Problem: 550. Game Play Analysis IV
-- Link: https://leetcode.com/problems/game-play-analysis-iv/
-- Difficulty: Medium
-- Topics: Database, Subquery, Join, Aggregation

-- Idea:
-- - Tìm ngày đăng nhập đầu tiên của mỗi player
-- - Kiểm tra xem player đó có đăng nhập lại đúng vào ngày hôm sau hay không
-- - Đếm số player thỏa điều kiện
-- - Chia cho tổng số player
-- - Làm tròn 2 chữ số thập phân

SELECT
    ROUND(
        COUNT(a.player_id) / COUNT(DISTINCT f.player_id),
        2
    ) AS fraction
FROM
    (
        SELECT
            player_id,
            MIN(event_date) AS first_login
        FROM Activity
        GROUP BY player_id
    ) f
LEFT JOIN Activity a
    ON f.player_id = a.player_id
   AND a.event_date = DATE_ADD(f.first_login, INTERVAL 1 DAY);