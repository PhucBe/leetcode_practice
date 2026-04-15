-- Problem: 0196. Delete Duplicate Emails
-- Link: https://leetcode.com/problems/delete-duplicate-emails/
-- Difficulty: Easy
-- Topic: SQL, DELETE, Self Join
--
-- Idea:
-- - Dùng self join để ghép các dòng có cùng email
-- - Nếu một dòng có id lớn hơn dòng khác cùng email, thì đó là dòng trùng và phải xóa
-- - Kết quả là chỉ giữ lại dòng có id nhỏ nhất cho mỗi email
--
-- Notes:
-- - DELETE p1 FROM ... nghĩa là xóa các dòng thuộc alias p1
-- - Điều kiện p1.id > p2.id đảm bảo giữ lại dòng nhỏ nhất
-- - Đây là pattern xóa duplicate nhưng giữ bản ghi đầu tiên

DELETE p1
FROM Person p1
JOIN Person p2
    ON p1.email = p2.email
   AND p1.id > p2.id;

DELETE FROM Person
WHERE id NOT IN (
    SELECT id
    FROM (
        SELECT MIN(id) as id
        FROM Person
        GROUP BY email
    ) as t
);