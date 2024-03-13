-- Write a script that lists all the tables of a database in your MySQL server.
IF &1 IS NOT NULL THEN
	USE $1;
	SHOW TABLES;
