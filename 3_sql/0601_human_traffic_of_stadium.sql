-- Problem: 601. Human Traffic of Stadium
-- Link: https://leetcode.com/problems/human-traffic-of-stadium/
-- Difficulty: Hard
-- Topics: Database, Window Function, Gaps and Islands

-- Idea:
-- - Chỉ giữ những dòng có people >= 100
-- - Trong các dòng này, nếu id liên tiếp thì chúng thuộc cùng một nhóm
-- - Dùng công thức:
--       id - ROW_NUMBER()
--   để nhận diện các nhóm id liên tiếp
-- - Sau đó nhóm lại, chỉ giữ những nhóm có ít nhất 3 dòng
-- - Cuối cùng trả ra toàn bộ các dòng thuộc các nhóm hợp lệ

WITH filtered AS (
    SELECT
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
),
valid_groups AS (
    SELECT grp
    FROM filtered
    GROUP BY grp
    HAVING COUNT(*) >= 3
)
SELECT
    f.id,
    f.visit_date,
    f.people
FROM filtered f
JOIN valid_groups v
    ON f.grp = v.grp
ORDER BY f.visit_date;