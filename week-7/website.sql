-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `follower_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'test2','test','test',10,'2022-10-17 16:46:23'),(2,'no.2','test2','test2',5,'2022-10-17 16:47:50'),(3,'no.3','test3','test3',20,'2022-10-17 16:48:18'),(4,'no.4','test4','test4',50,'2022-10-17 16:48:28'),(5,'vmeklmkfv','dirk122119','secret',500,'2022-10-17 16:48:57'),(6,'陳冠守','dirk12211911','ddd',0,'2022-10-24 21:10:35'),(7,'robert','robert122119','122119',0,'2022-10-24 21:29:41'),(8,'Dirk','dirk','dirk',0,'2022-10-25 20:03:14'),(9,'testuser','testuser','testuser',0,'2022-10-26 09:10:06'),(10,'haha','haha','haha',0,'2022-10-28 14:50:11'),(11,'wahaha','wahaha','wahaha',0,'2022-10-28 14:55:20'),(12,'wakuwaku','wakuwaku','wakuwaku',0,'2022-10-29 16:24:44');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `member_id` bigint NOT NULL,
  `content` varchar(255) NOT NULL,
  `like_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,1,'good',100,'2022-10-17 17:37:07'),(2,1,'nice',130,'2022-10-17 17:37:20'),(3,1,'have a nice today',330,'2022-10-17 17:37:37'),(4,2,'How are you?',334,'2022-10-17 17:38:02'),(6,3,'test id 0',20,'2022-10-19 17:38:53'),(7,5,'ddd',0,'2022-10-25 11:19:04'),(8,5,'test',0,'2022-10-25 11:19:08'),(9,5,'haha',0,'2022-10-25 11:19:22'),(10,7,'test',0,'2022-10-25 11:19:56'),(11,5,'dkmjaknvakfji',0,'2022-10-25 11:23:01'),(12,8,'Hello,I\'m dirk 41',0,'2022-10-25 20:05:45'),(13,5,'hi,dirk',0,'2022-10-26 09:09:47'),(14,9,'hi，I\'m testuser',0,'2022-10-26 09:10:32'),(16,5,'sss',0,'2022-10-28 14:46:32'),(17,10,'hahaha',0,'2022-10-28 14:50:22'),(18,11,'wahaha',0,'2022-10-28 14:55:26'),(19,12,'wakuwaku',0,'2022-10-29 16:24:57');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-02 18:04:24
