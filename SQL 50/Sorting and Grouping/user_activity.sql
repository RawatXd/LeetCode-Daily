-- User Activity for the past 30 days

Select 
 activity_date as day ,
 Count(Distinct user_id) as active_users
From Activity 
Where activity_date > '2019-06-27' AND activity_date <= '2019-07-27'
Group By activity_date ;