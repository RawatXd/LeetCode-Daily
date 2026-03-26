--User ID with at least 50 orders
Select 
 user_id ,
 Count(follower_id) as followers_count 
From Followers 
Group By user_id 
Order By user_id asc;