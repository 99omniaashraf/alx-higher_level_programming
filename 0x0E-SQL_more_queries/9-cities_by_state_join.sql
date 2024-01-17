-- Use INNER JOIN
SELECT a.id AS id, a.name AS name, b.name AS name
FROM cities a
INNER JOIN states b
ON a.state_id = b.id
ORDER BY a.id ASC;
