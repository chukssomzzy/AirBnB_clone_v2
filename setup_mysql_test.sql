-- prepares a MySQL server for the project  

-- CREATE THE DATABASE 
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- create a new user 
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwdsoMM1978#';

-- grant all privileges on `hbnb_test_db`
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- grant select privilege on performance_schema 
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
