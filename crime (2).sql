-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 10, 2020 at 09:27 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `crime`
--

-- --------------------------------------------------------

--
-- Table structure for table `complaint`
--

CREATE TABLE IF NOT EXISTS `complaint` (
  `compid` int(11) NOT NULL AUTO_INCREMENT,
  `stationid` int(11) NOT NULL,
  `comptitle` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `file` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `cusid` int(11) NOT NULL,
  `reply` varchar(50) NOT NULL,
  PRIMARY KEY (`compid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `complaint`
--

INSERT INTO `complaint` (`compid`, `stationid`, `comptitle`, `description`, `file`, `status`, `date`, `cusid`, `reply`) VALUES
(5, 1, 'ff', 'scsd', 'static/MEDIA/photogrphr_588Mi9n.jpg', 'rejected', '2020-02-10', 1, 'dont know about this case'),
(6, 1, 'bbb', 'mm', 'static/MEDIA/legal.jpg', 'not approved', '2020-02-10', 1, '');

-- --------------------------------------------------------

--
-- Table structure for table `crimedetails`
--

CREATE TABLE IF NOT EXISTS `crimedetails` (
  `crimeid` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `location` varchar(50) NOT NULL,
  `ipc` varchar(50) NOT NULL,
  `victimname` varchar(50) NOT NULL,
  `suspectname` varchar(50) NOT NULL,
  `f1` varchar(300) NOT NULL,
  `stationid` int(11) NOT NULL,
  PRIMARY KEY (`crimeid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `crimedetails`
--

INSERT INTO `crimedetails` (`crimeid`, `type`, `description`, `date`, `location`, `ipc`, `victimname`, `suspectname`, `f1`, `stationid`) VALUES
(1, 'robbery', 'robbery done by vinu,vhgv', '2020-02-04', '45', '45', 'ann', 'priya', 'static/MEDIA/legal_jLeA4se.jpg', 1);

-- --------------------------------------------------------

--
-- Table structure for table `criminaldetails`
--

CREATE TABLE IF NOT EXISTS `criminaldetails` (
  `criminalid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `age` int(11) NOT NULL,
  `height` varchar(50) NOT NULL,
  `weight` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `addr` varchar(50) NOT NULL,
  `phno` varchar(50) NOT NULL,
  `nickname` varchar(50) NOT NULL,
  `complexion` varchar(50) NOT NULL,
  `crimetype` varchar(50) NOT NULL,
  `moperation` varchar(50) NOT NULL,
  `identification` varchar(50) NOT NULL,
  `photo` varchar(300) NOT NULL,
  `thumb` varchar(300) NOT NULL,
  `languages` varchar(50) NOT NULL,
  `nocrime` varchar(50) NOT NULL,
  `stationid` int(11) NOT NULL,
  PRIMARY KEY (`criminalid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `criminaldetails`
--

INSERT INTO `criminaldetails` (`criminalid`, `name`, `age`, `height`, `weight`, `gender`, `addr`, `phno`, `nickname`, `complexion`, `crimetype`, `moperation`, `identification`, `photo`, `thumb`, `languages`, `nocrime`, `stationid`) VALUES
(1, 'vinu', 35, '6.4', 'vinubhai', 'male', 'aaa', '9658745263', 'vinubhai', 'wheatish', 'robbery', 'bbb', 'mmm', 'static/MEDIA/professional-photographer_v0ji0qG.jpg', 'static/MEDIA/cap%20img3_mici1Cz.jpg', 'malayalam', '2', 1);

-- --------------------------------------------------------

--
-- Table structure for table `cusreg`
--

CREATE TABLE IF NOT EXISTS `cusreg` (
  `cusid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `addr` varchar(50) NOT NULL,
  `dob` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `dis` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phno` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  PRIMARY KEY (`cusid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `cusreg`
--

INSERT INTO `cusreg` (`cusid`, `name`, `addr`, `dob`, `gender`, `dis`, `email`, `phno`, `username`) VALUES
(1, 'manu', 'gggg', '2020-01-02', 'male', 'Ernakulam', 'manu@gmail.com', '9874563254', 'manu');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE IF NOT EXISTS `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `description` varchar(50) NOT NULL,
  `pdate` date NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `feedback`
--


-- --------------------------------------------------------

--
-- Table structure for table `filesendstation`
--

CREATE TABLE IF NOT EXISTS `filesendstation` (
  `fileid` int(11) NOT NULL AUTO_INCREMENT,
  `fromuser` varchar(50) NOT NULL,
  `touser` varchar(50) NOT NULL,
  `sub` varchar(50) NOT NULL,
  `file` varchar(300) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`fileid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `filesendstation`
--

INSERT INTO `filesendstation` (`fileid`, `fromuser`, `touser`, `sub`, `file`, `date`) VALUES
(1, '1', '1', 'regarding a case', 'static/MEDIA/frontpages.output_eIyflLf.pdf', '2020-03-06');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`, `type`, `status`) VALUES
('manu', 'manu', 'customer', 'not approved'),
('admin', 'admin', 'admin', 'approved'),
('south', 'south', 'station', 'approved'),
('john', 'john', 'DGP', 'approved');

-- --------------------------------------------------------

--
-- Table structure for table `missingitem`
--

CREATE TABLE IF NOT EXISTS `missingitem` (
  `missid` int(11) NOT NULL AUTO_INCREMENT,
  `itemname` varchar(50) NOT NULL,
  `missingdate` date NOT NULL,
  `description` varchar(50) NOT NULL,
  `phno` varchar(50) NOT NULL,
  `cdate` date NOT NULL,
  `cid` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  `sid` int(11) NOT NULL,
  `reply` varchar(50) NOT NULL,
  PRIMARY KEY (`missid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `missingitem`
--

INSERT INTO `missingitem` (`missid`, `itemname`, `missingdate`, `description`, `phno`, `cdate`, `cid`, `status`, `sid`, `reply`) VALUES
(1, 'bag', '2020-03-03', 'missing bag from bus', '9856326587', '2020-03-06', 1, 'not approved', 0, ''),
(2, 'bag', '2020-03-03', 'missing bag from bus', '9856326587', '2020-03-06', 1, 'not approved', 0, '');

-- --------------------------------------------------------

--
-- Table structure for table `station`
--

CREATE TABLE IF NOT EXISTS `station` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `stationcharge` varchar(50) NOT NULL,
  `addr` varchar(50) NOT NULL,
  `district` varchar(50) NOT NULL,
  `phno` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `station`
--

INSERT INTO `station` (`sid`, `name`, `stationcharge`, `addr`, `district`, `phno`, `email`, `username`) VALUES
(1, 'south', 'manu', 'south ps ernakulam', 'Ernakulam', '9874526326', 'south@gmail.com', 'south');

-- --------------------------------------------------------

--
-- Table structure for table `wantedlist`
--

CREATE TABLE IF NOT EXISTS `wantedlist` (
  `wid` int(11) NOT NULL AUTO_INCREMENT,
  `criminalid` int(11) NOT NULL,
  `description` varchar(50) NOT NULL,
  `stationid` int(11) NOT NULL,
  PRIMARY KEY (`wid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `wantedlist`
--

INSERT INTO `wantedlist` (`wid`, `criminalid`, `description`, `stationid`) VALUES
(1, 1, 'Included in Wanted list', 1);
