-- Use RIGHT JOIN
SELECT b.title, a.genre_id
FROM tv_show_genres a
RIGHT JOIN tv_shows b
ON a.show_id = b.id
ORDER BY b.title, a.genre_id ASC;
