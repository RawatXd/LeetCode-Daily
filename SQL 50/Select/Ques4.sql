--LeetCode Question 4
--Write an SQL query to find the id of all people who viewed their own post.

Select DISTINCT author_id as id 
From Views
where author_id = viewer_id 
Order BY id asc;