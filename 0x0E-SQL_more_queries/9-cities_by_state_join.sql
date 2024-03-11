-- Shows all cities contained in the database 
-- Groups result set by city ID
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;