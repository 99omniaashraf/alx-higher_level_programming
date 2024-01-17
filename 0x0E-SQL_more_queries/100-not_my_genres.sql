-- Select LEFT JOIN with where clausule
SELECT name
FROM tv_genres
WHERE name
NOT IN (SELECT a.name FROM tv_genres a
	RIGHT JOIN tv_show_genres b
	ON a.id = b.genre_id
	RIGHT JOIN tv_shows c
	ON b.show_id = c.id
	WHERE c.title = 'Dexter')
ORDER BY 1 ASC;
