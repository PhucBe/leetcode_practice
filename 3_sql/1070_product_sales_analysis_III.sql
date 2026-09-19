/*
Problem: 1070. Product Sales Analysis III
Link: https://leetcode.com/problems/product-sales-analysis-iii/
Difficulty: Medium
Topics: Database, SQL, GROUP BY, MIN, JOIN

Idea:
- Bài toán yêu cầu tìm tất cả các lần bán hàng xảy ra
  trong năm đầu tiên mà mỗi product xuất hiện trong bảng Sales.

- Với mỗi product_id:
    + Tìm year nhỏ nhất.
    + Đây chính là first_year của product đó.

- Có một điểm quan trọng:
    + Một product có thể có NHIỀU sales trong cùng first_year.
    + Vì vậy không thể chỉ GROUP BY product_id rồi lấy quantity, price.
    + Cần tìm first_year trước, sau đó JOIN ngược lại bảng Sales
      để lấy TẤT CẢ các dòng có year = first_year.

Các bước:

1. Tạo bảng tạm `first_year`:
   
       SELECT
           product_id,
           MIN(year) AS first_year
       FROM Sales
       GROUP BY product_id

   Ví dụ:

       product_id | first_year
       -----------+-----------
       100        | 2008
       200        | 2011

2. JOIN bảng Sales với kết quả trên:

       ON s.product_id = f.product_id
       AND s.year = f.first_year

   Điều này giúp giữ lại tất cả sales của product
   trong năm đầu tiên.

3. Lấy các cột cần trả về:
       product_id
       first_year
       quantity
       price

SQL:
*/

SELECT
    s.product_id,
    f.first_year,
    s.quantity,
    s.price
FROM Sales s
JOIN (
    SELECT
        product_id,
        MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
) f
    ON s.product_id = f.product_id
    AND s.year = f.first_year;