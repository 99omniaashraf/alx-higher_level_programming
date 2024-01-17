-- Create a table with UNIQUE Column
CREATE TABLE IF NOT EXISTS `unique_id`
(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
