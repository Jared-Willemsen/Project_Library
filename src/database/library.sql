-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


-- -----------------------------------------------------
-- Schema Library
-- -----------------------------------------------------
DROP DATABASE IF EXISTS Library;
CREATE SCHEMA IF NOT EXISTS `Library` DEFAULT CHARACTER SET utf8 ;
USE `Library` ;


-- -----------------------------------------------------
-- Table `Library`.`Books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Books` (
  `book_id` INT NOT NULL,
  `title` VARCHAR(45) NULL,
  `author` VARCHAR(45) NULL,
  `genre` VARCHAR(45) NULL,
  `language` VARCHAR(45) NULL,
  PRIMARY KEY (`book_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Clients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Clients` (
  `client_id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `surname` VARCHAR(45) NOT NULL,
  `e_mail` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`client_id`),
  UNIQUE INDEX `client_id_UNIQUE` (`client_id` ASC) VISIBLE,
  UNIQUE INDEX `e_Mail_UNIQUE` (`e_mail` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Borrowings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Borrowings` (
  `borrowed_id` INT NOT NULL,
  `book_id` INT NOT NULL,
  `client_id` INT NOT NULL,
  `from_date` DATE NOT NULL,
  `to_date` DATE NULL,
  `extention` BINARY NOT NULL,
  PRIMARY KEY (`borrowed_id`),
  UNIQUE INDEX `idClients_UNIQUE` (`client_id` ASC) VISIBLE,
  UNIQUE INDEX `idBooks_UNIQUE` (`book_id` ASC) VISIBLE,
  UNIQUE INDEX `idLent_books_UNIQUE` (`borrowed_id` ASC) VISIBLE,
  CONSTRAINT `book_id`
    FOREIGN KEY (`book_id`)
    REFERENCES `Library`.`Books` (`book_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Client_Id`
    FOREIGN KEY (`client_id`)
    REFERENCES `Library`.`Clients` (`client_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Reservings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Reservings` (
  `reserved_id` INT NOT NULL,
  `client_id` INT NOT NULL,
  `book_id` INT NOT NULL,
  `from_date` DATE NOT NULL,
  `to_date` DATE NULL,
  PRIMARY KEY (`reserved_id`),
  UNIQUE INDEX `idClients_UNIQUE` (`client_id` ASC) VISIBLE,
  UNIQUE INDEX `idReserved_UNIQUE` (`reserved_id` ASC) VISIBLE,
  UNIQUE INDEX `idBooks_UNIQUE` (`book_id` ASC) VISIBLE,
  CONSTRAINT `books_id`
    FOREIGN KEY (`book_id`)
    REFERENCES `Library`.`Books` (`book_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `clients_id`
    FOREIGN KEY (`client_id`)
    REFERENCES `Library`.`Clients` (`client_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Employees`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Employees` (
  `employee_id` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Surname` VARCHAR(45) NULL,
  `E-mail` VARCHAR(45) NULL,
  `Password` VARCHAR(45) NULL,
  PRIMARY KEY (`employee_id`),
  UNIQUE INDEX `idEmployees_UNIQUE` (`employee_id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Jobs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Jobs` (
  `job_id` INT NOT NULL,
  `employee_id` INT NOT NULL,
  `Title` VARCHAR(45) NOT NULL,
  `from_date` DATE NOT NULL,
  `to_date` DATE NULL,
  PRIMARY KEY (`job_id`),
  UNIQUE INDEX `idEmployee-Jobs_UNIQUE` (`job_id` ASC) VISIBLE,
  UNIQUE INDEX `employee_id_UNIQUE` (`employee_id` ASC) VISIBLE,
  CONSTRAINT `employee_id`
    FOREIGN KEY (`employee_id`)
    REFERENCES `Library`.`Employees` (`employee_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Insert Data for books
-- -----------------------------------------------------
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1001, 'The Great Adventure', 'John Smith', 'Adventure', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1002, 'Mystery Mansion', 'Emily Johnson', 'Mystery', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1003, 'Fantasy Quest', 'David Brown', 'Fantasy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1004, 'Science Explorers', 'John Smith', 'Science Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1005, 'Romantic Escapade', 'Sophia Davis', 'Romance', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1006, 'The Thriller Code', 'Michael Anderson', 'Thriller', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1007, 'Historical Chronicles', 'Sarah Thompson', 'Historical Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1008, 'The Comedy Club', 'Andrew Wilson', 'Comedy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1009, 'Dystopian World', 'Jennifer Adams', 'Dystopian', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1010, 'Classic Tales', 'William Roberts', 'Classic', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1011, 'Whodunit Mystery', 'Emily Johnson', 'Mystery', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1012, 'The Magical Journey', 'Robert Harris', 'Fantasy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1013, 'Space Odyssey', 'John Smith', 'Science Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1014, 'Love in Paris', 'Sophia Davis', 'Romance', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1015, 'Mind Games', 'Michael Anderson', 'Thriller', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1016, 'Medieval Times', 'Sarah Thompson', 'Historical Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1017, 'Laugh Out Loud', 'Andrew Wilson', 'Comedy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1018, 'Post-Apocalyptic World', 'Jennifer Adams', 'Dystopian', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1019, 'Literary Masterpieces', 'William Roberts', 'Classic', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1020, 'Secrets Unveiled', 'Emily Johnson', 'Mystery', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1021, 'Enchanted Forest', 'Robert Harris', 'Fantasy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1022, 'Alien Encounters', 'John Smith', 'Science Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1023, 'Love at First Sight', 'Sophia Davis', 'Romance', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1024, 'The Hidden Agenda', 'Michael Anderson', 'Thriller', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1025, 'Ancient Empires', 'Sarah Thompson', 'Historical Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1026, 'Funny Fiasco', 'Andrew Wilson', 'Comedy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1027, 'Survival Instincts', 'Jennifer Adams', 'Dystopian', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1028, 'Literary Classics Revisited', 'William Roberts', 'Classic', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1029, 'Cryptic Clues', 'Emily Johnson', 'Mystery', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1030, 'Kingdom of Magic', 'Robert Harris', 'Fantasy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1031, 'Robots and Androids', 'John Smith', 'Science Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1032, 'Love on the Beach', 'Sophia Davis', 'Romance', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1033, "The Mind's Eye", 'Michael Anderson', 'Thriller', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1034, 'Revolutionary Times', 'Sarah Thompson', 'Historical Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1035, 'Comical Capers', 'Andrew Wilson', 'Comedy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1036, 'After the Cataclysm', 'Jennifer Adams', 'Dystopian', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1037, 'Literary Gems', 'William Roberts', 'Classic', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1038, 'Case of the Missing Diamond', 'Emily Johnson', 'Mystery', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1039, 'Wizards and Wonders', 'Robert Harris', 'Fantasy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1040, 'Interstellar Adventures', 'John Smith', 'Science Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1041, 'Love in the Countryside', 'Sophia Davis', 'Romance', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1042, 'The Silent Witness', 'Michael Anderson', 'Thriller', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1043, 'Time Traveler Chronicles', 'Sarah Thompson', 'Historical Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1044, 'Comedy Central', 'Andrew Wilson', 'Comedy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1045, 'Surviving the Apocalypse', 'Jennifer Adams', 'Dystopian', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1046, 'Literary Treasures', 'William Roberts', 'Classic', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1047, 'Fatal Betrayal', 'Emily Johnson', 'Mystery', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1048, 'Realm of Dragons', 'Robert Harris', 'Fantasy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1049, 'Parallel Universes', 'John Smith', 'Science Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1050, 'Love in the Alps', 'Sophia Davis', 'Romance', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1051, 'The Dark Secret', 'Michael Anderson', 'Thriller', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1052, 'Revolutionary War Chronicles', 'Sarah Thompson', 'Historical Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1053, 'Laugh Riot', 'Andrew Wilson', 'Comedy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1054, 'The Last Refuge', 'Jennifer Adams', 'Dystopian', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1055, 'Shakespearean Delights', 'William Roberts', 'Classic', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1056, 'The Haunted Manor', 'Emily Johnson', 'Mystery', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1057, 'Land of Magic', 'Robert Harris', 'Fantasy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1058, 'Exoplanetary Explorers', 'John Smith', 'Science Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1059, 'Love in the Wilderness', 'Sophia Davis', 'Romance', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1060, 'The Mysterious Stranger', 'Michael Anderson', 'Thriller', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1061, 'Renaissance Chronicles', 'Sarah Thompson', 'Historical Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1062, 'Comic Caper', 'Andrew Wilson', 'Comedy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1063, 'Beyond the Ruins', 'Jennifer Adams', 'Dystopian', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1064, 'Literary Reflections', 'William Roberts', 'Classic', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1065, 'The Stolen Artifact', 'Emily Johnson', 'Mystery', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1066, 'Realm of Sorcery', 'Robert Harris', 'Fantasy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1067, 'Cosmic Adventures', 'John Smith', 'Science Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1068, 'Love Under the Stars', 'Sophia Davis', 'Romance', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1069, 'The Final Showdown', 'Jane Anderson', 'Thriller', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1070, 'Lost in Time', 'Sarah Thompson', 'Historical Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1071, 'Laugh-a-Palooza', 'Andrew Wilson', 'Comedy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1072, 'Apocalyptic Chronicles', 'Jennifer Adams', 'Dystopian', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1073, 'Classic Adventures', 'William Roberts', 'Classic', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1074, 'The Enigma Files', 'Emily Johnson', 'Mystery', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1075, 'Mythical Realms', 'Robert Harris', 'Fantasy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1076, 'Galaxy Explorers', 'John Smith', 'Science Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1077, 'Love in the Rain', 'Sophia Davis', 'Romance', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1078, 'The Conspiracy Theory', 'Michael Anderson', 'Thriller', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1079, 'Victorian Era Chronicles', 'Sarah Thompson', 'Historical Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1080, 'Jokes and Pranks', 'Andrew Wilson', 'Comedy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1081, 'The New World', 'Jennifer Adams', 'Dystopian', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1082, 'Literary Escapades', 'William Roberts', 'Classic', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1083, 'The Puzzle Master', 'Emily Johnson', 'Mystery', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1084, 'Enchanted Kingdom', 'Robert Harris', 'Fantasy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1085, 'Space Odyssey II', 'John Smith', 'Science Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1086, 'Love in the City', 'Sophia Davis', 'Romance', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1087, 'The Dark Shadows', 'Michael Anderson', 'Thriller', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1088, 'Revolutionary Tales', 'Sarah Thompson', 'Historical Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1089, 'Comedy Bonanza', 'Andrew Wilson', 'Comedy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1090, 'The Last Hope', 'Jennifer Adams', 'Dystopian', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1091, 'Literary Odyssey', 'William Roberts', 'Classic', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1092, 'The Secret Society', 'Emily Johnson', 'Mystery', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1093, 'Realm of Magic', 'Robert Harris', 'Fantasy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1094, 'Astro Adventures', 'John Smith', 'Science Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1095, 'Love in the Woods', 'Sophia Davis', 'Romance', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1096, 'The Betrayed', 'Michael Anderson', 'Thriller', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1097, 'Medieval Tales', 'Sarah Thompson', 'Historical Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1098, 'Comedy Mania', 'Andrew Wilson', 'Comedy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1099, 'The Final Countdown', 'Jennifer Adams', 'Dystopian', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1100, 'Classic Revival', 'William Roberts', 'Classic', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1101, 'The Secret Agent', 'Emily Johnson', 'Mystery', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1102, 'Magical Realms', 'Robert Harris', 'Fantasy', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1103, 'Interstellar Encounters', 'John Smith', 'Science Fiction', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1104, 'Love in the City II', 'Sophia Davis', 'Romance', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1105, 'The Final Revelation', 'Michael Anderson', 'Thriller', 'English');
INSERT INTO Books(book_id, title, author, genre, language)
VALUES (1106, 'Victorian Chronicles', 'Sarah Thompson', 'Historical Fiction', 'English');



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;