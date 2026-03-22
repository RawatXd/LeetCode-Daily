--MOnthly transactions 1 

Select 
 DATE_FORMAT(trans_date , '%Y-%m') as month ,
 country , 
 count(id) as trans_count ,
 SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) as approved_count ,
 SUM(amount) as trans_total_amount ,
  Sum(CASE WHEN state = 'approved' THEN amount ELSE 0 END ) as approved_total_amount 

FROM Transactions
Group BY month , country ;
