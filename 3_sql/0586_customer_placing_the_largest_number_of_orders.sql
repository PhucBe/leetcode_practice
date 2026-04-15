-- Problem: 586. Customer Placing the Largest Number of Orders
-- Link: https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
-- Difficulty: Easy
-- Topics: Database, Group By, Order By, Limit

-- Idea:
-- - Đếm số đơn hàng của từng customer
-- - Sắp xếp theo số đơn hàng giảm dần
-- - Lấy customer đứng đầu
-- - Đề bài đảm bảo chỉ có đúng 1 customer có số đơn lớn nhất

SELECT customer_number
FROM (
    SELECT
        customer_number,
        COUNT(*) AS order_count
    FROM Orders
    GROUP BY customer_number
) t
ORDER BY order_count DESC
LIMIT 1;