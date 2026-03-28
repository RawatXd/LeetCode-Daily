--Select primary department for each employee.

Select 
employee_id,
department_id
From Employee
where primary_flag = 'Y'

UNION

Select employee_id , department_id
From Employee
Group BY employee_id 
Having Count(employee_id) = 1 ;