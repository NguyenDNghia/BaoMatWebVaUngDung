-- Done by Nghĩa
CREATE DATABASE IF NOT EXISTS `loginbaomatweb`;
USE `loginbaomatweb`;

CREATE TABLE users (
  id INT(11) AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL,
  phone VARCHAR(15) NOT NULL,
  password VARCHAR(255) NOT NULL
);