-- Problem: 602. Friend Requests II: Who Has the Most Friends
-- Link: https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/
-- Difficulty: Medium
-- Topics: Database, Union All, Group By, Order By

-- Idea:
-- - Mỗi dòng trong RequestAccepted biểu diễn một quan hệ bạn bè giữa 2 người
-- - Vì tình bạn là 2 chiều:
--     + requester_id có thêm 1 người bạn
--     + accepter_id cũng có thêm 1 người bạn
-- - Tách mỗi quan hệ thành 2 dòng bằng UNION ALL
-- - Sau đó đếm số bạn của từng người
-- - Sắp xếp giảm dần theo số bạn và lấy người đứng đầu
-- - Đề bài đảm bảo chỉ có đúng 1 người có nhiều bạn nhất

SELECT
    id,
    COUNT(*) AS num
FROM (
    SELECT requester_id AS id
    FROM RequestAccepted

    UNION ALL

    SELECT accepter_id AS id
    FROM RequestAccepted
) t
GROUP BY id
ORDER BY num DESC
LIMIT 1;