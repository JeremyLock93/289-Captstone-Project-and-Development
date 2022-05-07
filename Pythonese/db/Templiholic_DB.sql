-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: templiholics_db
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `files`
--

DROP TABLE IF EXISTS `files`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `files` (
  `FID` int NOT NULL AUTO_INCREMENT,
  `FileName` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8_swedish_ci NOT NULL,
  `FileLocation` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8_swedish_ci NOT NULL,
  `UploadDate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`FID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `files`
--

LOCK TABLES `files` WRITE;
/*!40000 ALTER TABLE `files` DISABLE KEYS */;
/*!40000 ALTER TABLE `files` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `templatedata`
--

DROP TABLE IF EXISTS `templatedata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `templatedata` (
  `AID` int NOT NULL AUTO_INCREMENT,
  `TID` int NOT NULL,
  `AssignmentName` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8_swedish_ci NOT NULL,
  `DueDate` datetime NOT NULL,
  `Comments` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8_swedish_ci NOT NULL,
  PRIMARY KEY (`AID`),
  KEY `TID_idx` (`TID`),
  KEY `TIDs_idx` (`TID`),
  CONSTRAINT `TIDs` FOREIGN KEY (`TID`) REFERENCES `templates` (`TID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `templatedata`
--

LOCK TABLES `templatedata` WRITE;
/*!40000 ALTER TABLE `templatedata` DISABLE KEYS */;
/*!40000 ALTER TABLE `templatedata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `templates`
--

DROP TABLE IF EXISTS `templates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `templates` (
  `TID` int NOT NULL AUTO_INCREMENT,
  `ClassName` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8_swedish_ci NOT NULL,
  `CreationDate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `File_location` varchar(150) COLLATE utf8_swedish_ci NOT NULL,
  PRIMARY KEY (`TID`),
  UNIQUE KEY `TID_UNIQUE` (`TID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `templates`
--

LOCK TABLES `templates` WRITE;
/*!40000 ALTER TABLE `templates` DISABLE KEYS */;
/*!40000 ALTER TABLE `templates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userfiles`
--

DROP TABLE IF EXISTS `userfiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userfiles` (
  `Record` int NOT NULL AUTO_INCREMENT,
  `USID` int NOT NULL,
  `FID` int NOT NULL,
  PRIMARY KEY (`Record`),
  KEY `USID_files_idx` (`USID`),
  KEY `FID_files_idx` (`FID`),
  CONSTRAINT `FID_files` FOREIGN KEY (`FID`) REFERENCES `files` (`FID`),
  CONSTRAINT `USID_files` FOREIGN KEY (`USID`) REFERENCES `users` (`USID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userfiles`
--

LOCK TABLES `userfiles` WRITE;
/*!40000 ALTER TABLE `userfiles` DISABLE KEYS */;
/*!40000 ALTER TABLE `userfiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `USID` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(15) CHARACTER SET utf8mb3 COLLATE utf8_swedish_ci NOT NULL,
  `LastName` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8_swedish_ci NOT NULL,
  `FirstName` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8_swedish_ci NOT NULL,
  `Email` varchar(155) CHARACTER SET utf8mb3 COLLATE utf8_swedish_ci NOT NULL,
  `Password` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8_swedish_ci NOT NULL,
  `Affiliation` char(1) CHARACTER SET utf8mb3 COLLATE utf8_swedish_ci NOT NULL,
  `DateCreated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`USID`),
  UNIQUE KEY `USID_UNIQUE` (`USID`),
  UNIQUE KEY `Username_UNIQUE` (`Username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Admin','admin','admin','admin@admin.com','$2b$12$yMeAL5i1NCOluMYsYnFZIOsFb2.uQG7ui4oHVShoQTji6tcoUCu92','A','2022-05-07 07:17:43');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usertemplates`
--

DROP TABLE IF EXISTS `usertemplates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usertemplates` (
  `Record` int NOT NULL AUTO_INCREMENT,
  `USID` int NOT NULL,
  `TID` int NOT NULL,
  PRIMARY KEY (`Record`),
  UNIQUE KEY `Record_UNIQUE` (`Record`),
  KEY `USID_user_idx` (`USID`),
  KEY `TID_user_idx` (`TID`),
  CONSTRAINT `TID_user` FOREIGN KEY (`TID`) REFERENCES `templates` (`TID`),
  CONSTRAINT `USID_user` FOREIGN KEY (`USID`) REFERENCES `users` (`USID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usertemplates`
--

LOCK TABLES `usertemplates` WRITE;
/*!40000 ALTER TABLE `usertemplates` DISABLE KEYS */;
/*!40000 ALTER TABLE `usertemplates` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-07  4:42:49
