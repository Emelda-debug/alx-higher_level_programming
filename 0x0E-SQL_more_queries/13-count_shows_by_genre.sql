-- script that lists all genres from hbtn_0d_tvshows and 
-- displays the number of shows linked to each.
-- each record will display: <TV Show genre> - <Number of shows linked to this genre>
-- First column - genre
-- Second column  - number_of_shows

SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genres RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
