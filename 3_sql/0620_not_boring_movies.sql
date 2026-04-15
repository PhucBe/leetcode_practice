-- Problem: 620. Not Boring Movies
-- Link: https://leetcode.com/problems/not-boring-movies/
-- Difficulty: Easy
-- Topics: Database, Filter, Order By

-- Idea:
-- - Chỉ lấy những phim có id lẻ
-- - Đồng thời description khác "boring"
-- - Sau đó sắp xếp theo rating giảm dần

SELECT
    id,
    movie,
    description,
    rating
FROM Cinema
WHERE id % 2 = 1
  AND description != 'boring'
ORDER BY rating DESC;