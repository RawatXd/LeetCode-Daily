--Replace Employee Id with Unique Identifier

Select 
  eu.unique_id ,
  e.name
From Employees e 
Left Join EmployeeUNI eu 
 on eu.id = e.id;