-- list score and name
SELECT score, name FROM second_tbale HAVING name IS NOT NULL ORDER BY score DESC;
