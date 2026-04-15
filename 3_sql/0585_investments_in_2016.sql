-- Problem: 585. Investments in 2016
-- Link: https://leetcode.com/problems/investments-in-2016/
-- Difficulty: Medium
-- Topics: Database, Group By, Having, Subquery

-- Idea:
-- - Chỉ lấy những policyholder thỏa 2 điều kiện:
--     + tiv_2015 xuất hiện từ 2 lần trở lên
--     + cặp (lat, lon) là duy nhất
-- - Dùng subquery thứ nhất để tìm các tiv_2015 bị trùng
-- - Dùng subquery thứ hai để tìm các location (lat, lon) là duy nhất
-- - Sau đó sum tiv_2016 của các dòng thỏa cả hai điều kiện
-- - Dùng ROUND(..., 2) để làm tròn 2 chữ số thập phân

SELECT
    ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
);