-- lists the number of records with the same score
-- The result should display the score and number of records for this score
--  label number
-- sorted by the number of records (descending)

SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC
