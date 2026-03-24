--No of unique subjects taught by each teacher

Select 
teacher_id ,
COUNT(Distinct subject_id) as cnt
From Teacher 
Group By teacher_id ;