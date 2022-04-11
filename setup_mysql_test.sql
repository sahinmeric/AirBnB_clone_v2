-- this script creates a database named hbnb_test_db
-- and creates a new user with all privilages on all the tables of hbnb_test_db
-- and select privilages on all the tables of performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO hbnb_test@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;
FLUSH PRIVILEGES;
