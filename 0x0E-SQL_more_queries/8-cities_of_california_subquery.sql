-- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.id, cities.name FROM cities INNER JOIN states ON states.id = cities.state_id WHERE states.name = "California";
