/*
Problem: 1068. Product Sales Analysis I
Link: https://leetcode.com/problems/product-sales-analysis-i/
Difficulty: Easy
Topics: Database, SQL, JOIN

Idea:
- Cần lấy:
    + product_name từ bảng Product
    + year và price từ bảng Sales
- Sales chỉ có product_id, không có product_name.
- Product có product_id và product_name.
- Hai bảng liên kết với nhau thông qua product_id.
- Vì mỗi sale trong Sales đều tham chiếu đến một product
  nên dùng INNER JOIN để ghép 2 bảng.
- Sau khi JOIN:
    + Product.product_name -> product_name
    + Sales.year -> year
    + Sales.price -> price

SQL:
    SELECT
        p.product_name,
        s.year,
        s.price
    FROM Sales s
    JOIN Product p
        ON s.product_id = p.product_id;

Time Complexity: O(n)
Space Complexity: O(n)
*/
SELECT
    p.product_name,
    s.year,
    s.price
FROM Sales s
JOIN Product p
    ON s.product_id = p.product_id;