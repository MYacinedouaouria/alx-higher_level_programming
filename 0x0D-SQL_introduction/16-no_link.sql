-- this script lists all records of thetable second_table
-- it does not list rows without name value
-- display the score and name in this order
-- records are listed in descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
