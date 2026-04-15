-- Problem: 0175. Combine Two Tables
-- Link: https://leetcode.com/problems/combine-two-tables/
-- Difficulty: Easy
-- Topic: SQL JOIN
--
-- Idea:
-- Dùng LEFT JOIN để lấy tất cả person từ bảng Person
-- Ghép thông tin city, state từ bảng Address nếu có

SELECT 
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a
    ON p.personId = a.personId;