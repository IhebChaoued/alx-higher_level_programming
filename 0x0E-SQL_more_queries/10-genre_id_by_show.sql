-- List all shows that have at least one genre linked
SELECT tv_shows.title, tv_shows_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC, tv_shows_genres.id ASC;
