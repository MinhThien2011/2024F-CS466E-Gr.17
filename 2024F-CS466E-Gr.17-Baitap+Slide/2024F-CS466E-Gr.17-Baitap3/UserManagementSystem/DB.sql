CREATE DATABASE usermanagement CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'thien'@'localhost' IDENTIFIED BY 'thien2011';
GRANT ALL PRIVILEGES ON usermanagement.* TO 'thien'@'localhost';
FLUSH PRIVILEGES;
USE usermanagement;


DROP database usermanagement;