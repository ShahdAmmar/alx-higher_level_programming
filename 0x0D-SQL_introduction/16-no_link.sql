-- list score and name if name not equl NULL

SELECT score, name FROM second_tbale WHERE name IS NOT NULL AND name !='' ORDER BY score DESC;
