-- List all shows without the genre Comedy
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_genres ON tv_shows.id = tv_genres.show_id AND tv_genres.name = 'Comedy'
WHERE tv_genres.show_id IS NULL
ORDER BY tv_shows.title ASC;

