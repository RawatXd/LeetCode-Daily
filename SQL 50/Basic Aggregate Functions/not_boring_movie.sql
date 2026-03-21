-- Not Boring Movies
Select 
id , movie , description , rating
From Cinema
Where id % 2 != 0
 AND description != 'boring' 
Order by rating desc ;