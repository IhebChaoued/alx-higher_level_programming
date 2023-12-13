-- Create database, table and few other things.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCE states(ID),
	name VARCHAR(256) NOT NULL
);
