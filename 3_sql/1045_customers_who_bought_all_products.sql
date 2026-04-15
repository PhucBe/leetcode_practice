"""
Problem: 1045. Customers Who Bought All Products
Link: https://leetcode.com/problems/customers-who-bought-all-products/
Difficulty: Medium
Topics: Database, SQL

Idea:
- Ta cần tìm những customer đã mua tất cả product có trong bảng Product
- Với mỗi customer:
    + đếm số lượng product_key khác nhau mà họ đã mua
- Nếu số lượng đó bằng tổng số product trong bảng Product
  thì customer đó đã mua đầy đủ tất cả sản phẩm
- Vì bảng Customer có thể có dòng trùng nhau nên phải dùng COUNT(DISTINCT product_key)
- Dùng GROUP BY customer_id để gom theo từng khách hàng
- Dùng HAVING để lọc ra những customer thỏa điều kiện

Time Complexity: O(n)
Space Complexity: O(n)
"""
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (
    SELECT COUNT(*)
    FROM Product
);