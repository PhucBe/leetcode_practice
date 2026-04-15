-- Problem: 607. Sales Person
-- Link: https://leetcode.com/problems/sales-person/
-- Difficulty: Easy
-- Topics: Database, Join, Subquery, NOT IN

-- Idea:
-- - Cần tìm salesperson không có bất kỳ order nào liên quan đến company tên "RED"
-- - Trước hết tìm các sales_id đã từng bán cho company "RED"
-- - Sau đó lấy những salesperson có sales_id không nằm trong tập đó

SELECT
    name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT o.sales_id
    FROM Orders o
    JOIN Company c
        ON o.com_id = c.com_id
    WHERE c.name = 'RED'
);
