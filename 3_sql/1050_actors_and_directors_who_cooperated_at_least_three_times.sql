"""
Problem: 1050. Actors and Directors Who Cooperated At Least Three Times
Link: https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/
Difficulty: Easy
Topics: Database, SQL

Idea:
- Ta cần tìm các cặp (actor_id, director_id) đã hợp tác với nhau ít nhất 3 lần
- Mỗi dòng trong bảng biểu diễn 1 lần hợp tác
- Vì vậy:
    + gom nhóm theo actor_id và director_id
    + đếm số dòng trong mỗi nhóm
- Nếu số lần hợp tác >= 3 thì lấy cặp đó ra
- Dùng GROUP BY để gom nhóm
- Dùng HAVING để lọc các nhóm có số lần xuất hiện thỏa điều kiện

Time Complexity: O(n)
Space Complexity: O(n)
"""
SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3;