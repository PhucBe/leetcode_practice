-- Problem: 0180. Consecutive Numbers
-- Link: https://leetcode.com/problems/consecutive-numbers/
-- Difficulty: Medium
-- Topic: SQL, Self Join
--
-- Idea:
-- - Join bảng Logs 3 lần để tạo ra 3 dòng liên tiếp theo id
-- - Kiểm tra num ở cả 3 dòng có bằng nhau hay không
-- - Dùng DISTINCT để tránh trả về trùng lặp
--
-- Notes:
-- - "Consecutively" nghĩa là phải liên tiếp theo id
-- - id trong đề là autoincrement, nên có thể dùng để xác định thứ tự
-- - Đây là pattern so sánh các dòng kề nhau trong SQL

SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2
    ON l1.id = l2.id - 1
JOIN Logs l3
    ON l2.id = l3.id - 1
WHERE l1.num = l2.num
  AND l2.num = l3.num;