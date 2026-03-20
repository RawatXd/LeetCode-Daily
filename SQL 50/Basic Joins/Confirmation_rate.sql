-- Confirmation Rate

Select 
s.user_id , 
ROUND(AVG(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END), 2) AS confirmation_rate
From Signups s 
LEFT JOIN Confirmations c
 on s.user_id = c.user_id
Group BY s.user_id ;