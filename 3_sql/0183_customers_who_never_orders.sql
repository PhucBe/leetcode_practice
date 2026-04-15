-- Problem: 0183. Customers Who Never Order
-- Link: https://leetcode.com/problems/customers-who-never-order/
-- Difficulty: Easy
-- Topic: SQL, LEFT JOIN
--
-- Idea:
-- - Giữ tất cả khách hàng bằng LEFT JOIN
-- - Ghép với Orders theo customer id
-- - Những khách hàng không có đơn hàng sẽ có cột từ Orders là NULL
-- - Lọc các dòng đó bằng WHERE o.id IS NULL
--
-- Notes:
-- - LEFT JOIN rất hữu ích khi cần tìm dữ liệu ở bảng trái không có bản ghi tương ứng ở bảng phải
-- - Đây là pattern "anti join" rất phổ biến

SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o
    ON c.id = o.customerId
WHERE o.id IS NULL;