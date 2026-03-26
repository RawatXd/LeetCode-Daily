--Class with at least 50 students

Select class From Courses 
Group BY class
HAVING CounT(student) >=5 ;