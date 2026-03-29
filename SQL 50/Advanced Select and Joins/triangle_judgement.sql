 -- Triangle Judgement

 Select 
x , y , z,
  CASE 
     when x + y > z AND x + z > y AND y + z > x then "Yes" 
     ELSE 'No' 
   End as triangle
FROM Triangle 
Group By x, y , z ;