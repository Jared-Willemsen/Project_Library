-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Library
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Library
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Library` DEFAULT CHARACTER SET utf8 ;
USE `Library` ;

-- -----------------------------------------------------
-- Table `Library`.`Books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Books` (
  `Book-Id` INT NOT NULL,
  `Title` VARCHAR(45) NULL,
  `Author` VARCHAR(45) NULL,
  `Genre` VARCHAR(45) NULL,
  `Language` VARCHAR(45) NULL,
  PRIMARY KEY (`Book-Id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Clients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Clients` (
  `Client-Id` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Surname` VARCHAR(45) NOT NULL,
  `E-Mail` VARCHAR(45) NOT NULL,
  `Password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Client-Id`),
  UNIQUE INDEX `Client-Id_UNIQUE` (`Client-Id` ASC) VISIBLE,
  UNIQUE INDEX `E-Mail_UNIQUE` (`E-Mail` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Borrowings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Borrowings` (
  `Borrowed-Id` INT NOT NULL,
  `Book-Id` INT NOT NULL,
  `Client-Id` INT NOT NULL,
  `From-Date` DATE NOT NULL,
  `To-Date` DATE NULL,
  `Extention` BINARY NOT NULL,
  PRIMARY KEY (`Borrowed-Id`),
  UNIQUE INDEX `idClients_UNIQUE` (`Client-Id` ASC) VISIBLE,
  UNIQUE INDEX `idBooks_UNIQUE` (`Book-Id` ASC) VISIBLE,
  UNIQUE INDEX `idLent_books_UNIQUE` (`Borrowed-Id` ASC) VISIBLE,
  CONSTRAINT `Book-Id`
    FOREIGN KEY (`Book-Id`)
    REFERENCES `Library`.`Books` (`Book-Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Client_Id`
    FOREIGN KEY (`Client-Id`)
    REFERENCES `Library`.`Clients` (`Client-Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Reservings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Reservings` (
  `Reserved-Id` INT NOT NULL,
  `Client-Id` INT NOT NULL,
  `Book-Id` INT NOT NULL,
  `From-Date` DATE NOT NULL,
  `To_Date` DATE NULL,
  PRIMARY KEY (`Reserved-Id`),
  UNIQUE INDEX `idClients_UNIQUE` (`Client-Id` ASC) VISIBLE,
  UNIQUE INDEX `idReserved_UNIQUE` (`Reserved-Id` ASC) VISIBLE,
  UNIQUE INDEX `idBooks_UNIQUE` (`Book-Id` ASC) VISIBLE,
  CONSTRAINT `Books-Id`
    FOREIGN KEY (`Book-Id`)
    REFERENCES `Library`.`Books` (`Book-Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Clients-Id`
    FOREIGN KEY (`Client-Id`)
    REFERENCES `Library`.`Clients` (`Client-Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Employees`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Employees` (
  `Employee-Id` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Surname` VARCHAR(45) NULL,
  `E-mail` VARCHAR(45) NULL,
  `Password` VARCHAR(45) NULL,
  PRIMARY KEY (`Employee-Id`),
  UNIQUE INDEX `idEmployees_UNIQUE` (`Employee-Id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Jobs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Jobs` (
  `Job-Id` INT NOT NULL,
  `Employee-Id` INT NOT NULL,
  `Title` VARCHAR(45) NOT NULL,
  `From-Date` DATE NOT NULL,
  `To-Date` DATE NULL,
  PRIMARY KEY (`Job-Id`),
  UNIQUE INDEX `idEmployee-Jobs_UNIQUE` (`Job-Id` ASC) VISIBLE,
  UNIQUE INDEX `Employee-Id_UNIQUE` (`Employee-Id` ASC) VISIBLE,
  CONSTRAINT `Employee-Id`
    FOREIGN KEY (`Employee-Id`)
    REFERENCES `Library`.`Employees` (`Employee-Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
