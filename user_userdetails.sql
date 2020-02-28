-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 29, 2020 at 01:38 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dashboard`
--

-- --------------------------------------------------------

--
-- Table structure for table `user_userdetails`
--

CREATE TABLE `user_userdetails` (
  `adminID` int(11) NOT NULL,
  `adminName` varchar(50) NOT NULL,
  `adminEmail` varchar(50) NOT NULL,
  `adminPhone` varchar(11) NOT NULL,
  `adminUser` varchar(50) NOT NULL,
  `adminPass` varchar(100) NOT NULL,
  `adminRole` varchar(40) NOT NULL,
  `adminStatus` int(11) NOT NULL,
  `adminDT` datetime(6) NOT NULL,
  `adminPerms` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_userdetails`
--

INSERT INTO `user_userdetails` (`adminID`, `adminName`, `adminEmail`, `adminPhone`, `adminUser`, `adminPass`, `adminRole`, `adminStatus`, `adminDT`, `adminPerms`) VALUES
(2, 'Ashu', 'ashhuu28@gmail.com', '2147483647', 'ashhuu28', 'pbkdf2_sha256$180000$5cdvUyIMRrO9$XpmmV+f/HDLF2TcXcJ88NwFLj4WhrrJ3a88QYHxVu1s=', 'primary', 1, '2020-01-29 10:03:59.428284', 7),
(3, 'Abhijeet', 'ashhuu@gmail.com', '9874837329', 'Abhi123', 'pbkdf2_sha256$180000$S3qZDJ2mMYsI$RYCDILr4gHebYnt2R2TmaHGytoawYfsmdDNOMzqM9Y8=', 'primary', 1, '2020-01-29 12:37:47.550979', 7);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user_userdetails`
--
ALTER TABLE `user_userdetails`
  ADD PRIMARY KEY (`adminID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user_userdetails`
--
ALTER TABLE `user_userdetails`
  MODIFY `adminID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
