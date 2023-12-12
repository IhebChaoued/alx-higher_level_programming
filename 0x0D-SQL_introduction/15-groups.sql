-- Lists the number of records with the same score
SELECT score,
	count(*) AS number
FROM second_table
ORDER BY number DESC
