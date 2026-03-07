--LeetCode Question 3
--Write an SQL query to find the name, population and area of the countries in the World with a population greater than 25 million.

SELECT name , population , area from World
Where population >= 25000000
  OR area >= 3000000 ;