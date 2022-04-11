/*this script creates a database named hbnb_dev_db
and creates a new user with all privilages on all the tables of hbnb_dev_db
and select privilages on all the tables of performance_schema*/
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED WITH authentication_plugin BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
FLUSH PRIVILEGES;
