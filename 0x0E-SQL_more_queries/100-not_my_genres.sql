-- Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tv_genres.name FROM tv_genres WHERE tv_genres.id NOT IN (SELECT genre_id FROM tv_show_genres INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id WHERE tv_shows.title = 'Dexter') ORDER BY name ASC
