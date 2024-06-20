-- MySQL dump 10.13  Distrib 8.0.35, for Win64 (x86_64)
--
-- Host: localhost    Database: photo_management
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `annotations`
--

DROP TABLE IF EXISTS `annotations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `annotations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `photo_id` int NOT NULL,
  `annotation` text NOT NULL,
  `time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `photo_id` (`photo_id`),
  CONSTRAINT `annotations_ibfk_1` FOREIGN KEY (`photo_id`) REFERENCES `photos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `annotations`
--

LOCK TABLES `annotations` WRITE;
/*!40000 ALTER TABLE `annotations` DISABLE KEYS */;
INSERT INTO `annotations` VALUES (1,1,'漂亮','2024-06-09 08:00:08'),(2,1,'好看','2024-06-09 08:00:14'),(3,1,'这是湖光晚霞','2024-06-09 08:00:32'),(4,1,'这是很美的晚霞','2024-06-09 08:36:17'),(5,1,'嗯','2024-06-17 12:27:11'),(7,1,'好漂亮','2024-06-18 05:06:58'),(9,19,'山海','2024-06-19 22:20:28');
/*!40000 ALTER TABLE `annotations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `categories_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'风景照','这是一些风景照',1),(13,'建筑','这是一些建筑的照片',1),(14,'宠物','这是一些可爱宠物的照片',1),(15,'美食','这是一些美食',1),(16,'城市','这是一些城市照片',1),(17,'风景照','1',8),(18,'动物','1',8),(20,'城市','1',8),(21,'其他',NULL,1),(22,'图像生成',NULL,1),(23,'人像','1',1);
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `photos`
--

DROP TABLE IF EXISTS `photos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `photos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `category_id` int DEFAULT NULL,
  `file_path` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `photos_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `photos`
--

LOCK TABLES `photos` WRITE;
/*!40000 ALTER TABLE `photos` DISABLE KEYS */;
INSERT INTO `photos` VALUES (1,'湖光晚霞',1,'static\\upload\\cmy\\风景照\\cmy_风景照_湖光晚霞.jpg'),(19,'山海',1,'static/upload/cmy\\风景照\\cmy_风景照_山海.jpg'),(20,'晚霞公路',1,'static/upload/cmy\\风景照\\cmy_风景照_晚霞公路.jpg'),(21,'可爱小猫',14,'static/upload/cmy\\宠物\\cmy_宠物_可爱小猫.jpg'),(22,'川菜',15,'static/upload/cmy\\美食\\cmy_美食_川菜.jpg'),(23,'城市',16,'static/upload/cmy\\城市\\cmy_城市_城市.jpg'),(24,'建筑',13,'static/upload/cmy\\建筑\\cmy_建筑_建筑.jpg'),(25,'海边',17,'static/upload/lsy\\风景照\\lsy_风景照_海边.jpg'),(27,'山海',17,'static/upload/lsy\\风景照\\lsy_风景照_山海.jpg'),(28,'晚霞公路',17,'static/upload/lsy\\风景照\\lsy_风景照_晚霞公路.jpg'),(29,'雪',17,'static/upload/lsy\\风景照\\lsy_风景照_雪.jpg'),(30,'小猫',18,'static/upload/lsy\\动物\\lsy_动物_小猫.jpg'),(31,'湖光晚霞',17,'static/upload/lsy\\风景照\\lsy_风景照_湖光晚霞.jpg'),(35,'高楼大厦',20,'static/upload/lsy\\城市\\lsy_城市_高楼大厦.jpg'),(36,'小兔',21,'static/upload/cmy\\其他\\cmy_其他_小兔.jpg'),(37,'小兔小兔',22,'static/upload/generated\\cmy\\图像生成\\cmy_图像生成_小兔小兔.jpg'),(38,'兔',22,'static/upload/generated\\cmy\\图像生成\\cmy_图像生成_兔.jpg'),(39,'兔',22,'static/upload/generated\\cmy\\图像生成\\cmy_图像生成_兔.jpg'),(40,'tu',22,'static/upload/generated\\cmy\\图像生成\\cmy_图像生成_tu.jpg'),(41,'tu',22,'static/upload/generated\\cmy\\图像生成\\cmy_图像生成_tu.jpg'),(42,'rabbit',22,'static/upload/generated\\cmy\\图像生成\\cmy_图像生成_rabbit.jpg'),(43,'刘亦菲',23,'static/upload/cmy\\人像\\cmy_人像_刘亦菲.jpg');
/*!40000 ALTER TABLE `photos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'cmy','123'),(2,'hi','123'),(3,'lalababa','123456'),(4,'laba','123'),(5,'ll','111'),(6,'lbz','123'),(7,'sh','123'),(8,'lsy','123'),(9,'bzx','123');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-20 17:50:28
