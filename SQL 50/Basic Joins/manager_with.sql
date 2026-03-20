--Manager with atleast 5 direct reports
Select e.name 
From Employee e 
JOIN Employee m 
 on e.id = m.managerId
Group BY e.id , e.name
Having count(e.id)>=5 ;