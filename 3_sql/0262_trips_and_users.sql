-- Problem: 0262. Trips and Users
-- Link: https://leetcode.com/problems/trips-and-users/
-- Difficulty: Hard
-- Topic: SQL, JOIN, CASE, GROUP BY, AVG
--
-- Idea:
-- - Join Trips với Users hai lần để kiểm tra cả client và driver đều không banned
-- - Chỉ lấy các trip trong khoảng 2013-10-01 đến 2013-10-03
-- - Biến trip bị cancel thành 1, completed thành 0
-- - AVG của các giá trị 0/1 chính là cancellation rate
-- - ROUND(..., 2) để làm tròn 2 chữ số thập phân
--
-- Notes:
-- - Phải lọc cả client và driver đều unbanned
-- - status != 'completed' nghĩa là canceled
-- - AVG(CASE...) là mẹo rất hay cho các bài tính tỷ lệ

SELECT
    t.request_at AS Day,
    ROUND(
        AVG(
            CASE
                WHEN t.status != 'completed' THEN 1
                ELSE 0
            END
        ),
        2
    ) AS `Cancellation Rate`
FROM Trips t
JOIN Users c
    ON t.client_id = c.users_id
JOIN Users d
    ON t.driver_id = d.users_id
WHERE c.banned = 'No'
  AND d.banned = 'No'
  AND t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at;

SELECT
    t.request_at AS Day,
    ROUND(
        SUM(CASE 
              WHEN t.status IN ('cancelled_by_client', 'cancelled_by_driver')
              THEN 1 ELSE 0 
            END) / COUNT(*),
        2
    ) AS "Cancellation Rate"
FROM Trips t
JOIN Users c
    ON t.client_id = c.users_id
   AND c.banned = 'No'
   AND c.role = 'client'
JOIN Users d
    ON t.driver_id = d.users_id
   AND d.banned = 'No'
   AND d.role = 'driver'
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at
ORDER BY t.request_at;