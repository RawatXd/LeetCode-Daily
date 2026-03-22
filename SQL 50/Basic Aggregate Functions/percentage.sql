 -- Percentage of User attended a Contest

Select 
r.contest_id , 
ROUND(COUNT(r.user_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2) as percentage 
From Users u
Inner JOin Register r 
 on u.user_id = r.user_id 
Group BY contest_id
Order BY percentage desc ,contest_id asc ;