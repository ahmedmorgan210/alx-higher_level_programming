-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 13-count_shows_by_genre.sql)

-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

--     The tv_shows table contains only one record where title = Dexter (but the id can be different)
--     Each record should display: tv_genres.name
--     Results must be sorted in ascending order by the genre name
--     You can use only one SELECT statement
--     The database name will be passed as an argument of the mysql command
SELECT tv_genres.name AS "name"
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id= tv_shows.id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = "Dexter"
ORDER BY name ASC;