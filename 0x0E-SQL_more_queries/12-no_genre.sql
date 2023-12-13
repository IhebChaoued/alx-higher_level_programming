-- List all shows without a genre linked.
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
