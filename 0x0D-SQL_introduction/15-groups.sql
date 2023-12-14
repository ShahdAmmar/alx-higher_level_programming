-- list records with same score
SELECT score, COUNT(*) As number from second_table GROUP BY score ORDER BY number DESC;
