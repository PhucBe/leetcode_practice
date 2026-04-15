-- Problem: 0197. Rising Temperature
-- Link: https://leetcode.com/problems/rising-temperature/
-- Difficulty: Easy
-- Topic: SQL, Self Join, Date
--
-- Idea:
-- - Dùng self join để ghép mỗi ngày với ngày hôm trước
-- - Điều kiện nối là recordDate của ngày hiện tại = recordDate hôm trước + 1 ngày
-- - Lọc những ngày có nhiệt độ cao hơn hôm trước
--
-- Notes:
-- - Phải so sánh theo recordDate, không dùng id
-- - Đây là pattern so sánh một dòng với dòng ngày trước đó

SELECT w1.id
FROM Weather w1
JOIN Weather w2
    ON w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)
WHERE w1.temperature > w2.temperature;