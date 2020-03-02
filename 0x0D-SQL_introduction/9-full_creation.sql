-- creates a table called second_table.
-- second_table:
-- id INT.
-- name VARCHAR(256).
-- score INT.
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);

INSERT INTO
	second_table (id, name, score)
VALUES
	(1, "jhon", 10),
	(2, "Alex", 3),
	(3, "Bob", 14),
	(4, "George", 8);