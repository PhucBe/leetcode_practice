-- Problem: 608. Tree Node
-- Link: https://leetcode.com/problems/tree-node/
-- Difficulty: Medium
-- Topics: Database, CASE, Subquery

-- Idea:
-- - Nếu p_id IS NULL => node gốc => Root
-- - Nếu id không xuất hiện trong cột p_id của bất kỳ dòng nào khác => không có con => Leaf
-- - Còn lại => Inner
-- - Dùng CASE WHEN để phân loại từng node

SELECT
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree;

SELECT
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id NOT IN (SELECT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Leaf'
        ELSE 'Inner'
    END AS type
FROM Tree;

SELECT
    t1.id,
    CASE
        WHEN t1.p_id IS NULL THEN 'Root'
        WHEN t2.id IS NULL THEN 'Leaf'
        ELSE 'Inner'
    END AS type
FROM Tree t1
LEFT JOIN Tree t2
    ON t1.id = t2.p_id
GROUP BY t1.id, t1.p_id;