-- LeetCode Ques2.sql
-- Find customers who are not referred by customer with id 2

SELECT name 
FROM  Customer 
Where referee_id != 2 or referee_id is NULL;