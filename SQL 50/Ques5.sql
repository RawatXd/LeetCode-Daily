--LeetCode Question 5
--Write an SQL query to find the id of all tweets that have content longer than 15

Select tweet_id 
FROM Tweets 
WHERE CHAR_LENGTH(content) > 15