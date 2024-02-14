-- script that creates the database hbtn_0d_usa and
--the table states (in the database hbtn_0d_usa)
--states description:
--id INT unique, auto generated, can’t be null and is a primary key
--name VARCHAR(256) can’t be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa
-- databse created above
USE hbtn_0d_usa;
--- table to be created using db
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
--table created

