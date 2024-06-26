-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 12-no_genre.sql)

-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

--     Each record should display: <TV Show genre> - <Number of shows linked to this genre>
--     First column must be called genre
--     Second column must be called number_of_shows
--     Don’t display a genre that doesn’t have any shows linked
--     Results must be sorted in descending order by the number of shows linked
--     You can use only one SELECT statement
--     The database name will be passed as an argument of the mysql command
SELECT tv_genres.name AS "genre", COUNT(tv_shows.title) AS "number_of_shows"
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
HAVING COUNT(tv_shows.title) > 0 AND tv_genres.name IS NOT NULL
ORDER BY number_of_shows DESC;