-- prepares a MySQL server for the project 

-- CREATE A DATABASE 
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

-- create a new user 
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant all privileges to new user 

GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- grant select priviledge on performance_schema db
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
