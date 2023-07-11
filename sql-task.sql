CREATE DATABASE foundation_assessment_ii;
USE foundation_assessment_ii;

-- movie id is int
-- name is varchar
-- length is datetime object
-- rating is varchar

-- id is int
-- four_k is bool

-- id is int
-- movie id int
-- screen id int
-- start time is datetime
-- seats is int 

CREATE TABLE movie_info (
movie_ID int,
Movie_Name varchar(255),
Movie_Length time,
Age_Rating varchar(255)
);

CREATE TABLE screens(
Screen_ID int,
Four_K bool);

CREATE TABLE showings (
Showing_ID int,
Movie_ID int,
Screen_ID int,
Start_Time time,
Available_Seats int
);

-- population

INSERT INTO movie_info(Movie_ID, Movie_Name, Movie_Length, Age_Rating)
 VALUES 
 (1, "The Movie", "2:19:00", "12A"),
 (2, "The Other Movie", "1:30:00", "15"),
 (3, "The 3D Amazing Movie",  "1:42:00", "PG"),
 (4, "La Allure", "1:09:00", "18"),
 (5, "The Cartoon", "1:15:00", "U"),
 (6, "The Scary Cartoon", "1:23:00", "PG"),
 (7, "The Coming Of Age", "1:40:00", "12A"),
 (8, "The War", "2:07:00", "15"),
 (9, "The Murder Mystery", "1:47:00", "15");


INSERT INTO screens(Screen_ID, Four_K)
 VALUES 
  (1, True),
  (2, False),
  (3, True),
  (4, True),
  (5, True),
  (6, True),
  (7, True),
  (8, False),
  (9, True),
  (10, True);
  
  
 INSERT INTO showings(Showing_ID, Movie_ID,Screen_ID, Start_Time, Available_Seats)
 VALUES 
  (1, 1, 2, '12:00:00', 10), 
  (2, 1, 2, '17:00:00', 23), 
  (3, 2, 9, '10:30:00', 30), 
  (4, 3, 1, '07:00:00', 38), 
  (5, 3, 5, '10:00:00', 26), 
  (6, 3, 1, '17:00:00', 5), 
  (7, 3, 1, '19:00:00', 0), 
  (8, 3, 5, '14:00:00', 2), 
  (9, 4, 9, '20:00:00', 14), 
  (10, 4, 9, '23:00:00', 23), 
  (11, 5, 6, '09:30:00', 30), 
  (12, 5, 6, '12:30:00', 7), 
  (13, 5, 6, '14:30:00', 0), 
  (14, 5, 6, '15:20:00', 0), 
  (15, 6, 10, '10:00:00', 32), 
  (16, 6, 10, '13:30:00', 25), 
  (17, 6, 10, '17:00:00', 14), 
  (18, 7, 7, '12:00:00', 36), 
  (19, 8, 4, '15:00:00', 24), 
  (20, 9, 3, '17:00:00', 0);

-- 4.2
-- select movie name and start time
SELECT m.Movie_Name, s.Start_Time
-- Extract name from the movie info table
FROM movie_info m
-- Join the showings start time and movie id 
JOIN showings s ON m.Movie_ID = s.Movie_ID
-- This is where the start time in the showings table is over noon
-- and seats >= 1
WHERE s.Start_Time > "12:00:00" AND s.Available_Seats >= 1
-- Ordered by time
ORDER BY s.Start_Time ASC;

-- 4.3 return movie name with most showings
-- this will be where the movie id shows up the most in the showings table

-- select name from movie info
SELECT Movie_Name 
FROM movie_info
-- where the id is the most common in the screening table
WHERE Movie_ID = (
SELECT Movie_ID
FROM showings
GROUP BY Movie_ID
ORDER BY COUNT(*) DESC
LIMIT 1
);





