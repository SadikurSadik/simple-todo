# ************************************************************
# Author: Sadikur Sadik
#
# Host: localhost (MySQL 5.7.38)
# Database: simple_todo_db
# Generation Time: 2023-06-09 11:48:19 +0000
# ************************************************************

CREATE DATABASE IF NOT EXISTS simple_todo_db;

USE simple_todo_db;


# Dump of table todos
# ------------------------------------------------------------

DROP TABLE IF EXISTS `todos`;

CREATE TABLE `todos` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `todo` varchar(255) NOT NULL,
  `is_completed` tinyint(1) DEFAULT '0',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `todos` WRITE;
/*!40000 ALTER TABLE `todos` DISABLE KEYS */;

INSERT INTO `todos` (`id`, `todo`, `is_completed`, `created_at`, `updated_at`)
VALUES
	(1,'Task One',0,'2023-06-09 15:47:30','2023-06-09 15:47:30'),
	(2,'Task Two',1,'2023-06-09 15:47:38','2023-06-09 15:47:49'),
	(3,'Task Three',0,'2023-06-09 15:47:46','2023-06-09 15:47:46');

/*!40000 ALTER TABLE `todos` ENABLE KEYS */;
UNLOCK TABLES;

