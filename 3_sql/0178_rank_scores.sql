-- Problem: 0178. Rank Scores
-- Link: https://leetcode.com/problems/rank-scores/
-- Difficulty: Medium
-- Topic: SQL, Window Function
-- Idea:
-- - Xếp hạng điểm từ cao xuống thấp
-- - Các điểm bằng nhau phải cùng rank
-- - Rank tiếp theo không được nhảy số
-- -> Dùng DENSE_RANK()
-- Notes:
-- - DENSE_RANK() phù hợp khi cần ranking không có holes
-- - Không dùng RANK() vì sẽ bị nhảy số sau tie
-- - Không dùng ROW_NUMBER() vì tie phải cùng rank

SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores
ORDER BY score DESC;