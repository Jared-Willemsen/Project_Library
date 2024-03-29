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
  `book_id` INT AUTO_INCREMENT NOT NULL,
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
  `client_id` INT AUTO_INCREMENT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `surname` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(128) NOT NULL,
  PRIMARY KEY (`client_id`),
  UNIQUE INDEX `client_id_UNIQUE` (`client_id` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Borrowings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Borrowings` (
  `borrowed_id` INT AUTO_INCREMENT NOT NULL,
  `book_id` INT NOT NULL,
  `client_id` INT NOT NULL,
  `from_date` DATE NOT NULL,
  `to_date` DATE NULL,
  `due_date` DATE NULL,
  `extention` TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`borrowed_id`),
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
-- Table `Library`.`Employees`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Employees` (
  `employee_id` INT AUTO_INCREMENT NOT NULL,
  `name` VARCHAR(45) NULL,
  `surname` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(128) NULL,
  PRIMARY KEY (`employee_id`),
  UNIQUE INDEX `idEmployees_UNIQUE` (`employee_id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`Jobs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Jobs` (
  `job_id` INT AUTO_INCREMENT NOT NULL,
  `employee_id` INT NOT NULL,
  `title` VARCHAR(45) NOT NULL,
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
-- Table `Library`.`Password_reset_tokens`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Password_reset_tokens` (
  `employee_id` INT NOT NULL,
  `token` VARCHAR(128) NOT NULL UNIQUE,
  `token_expiry` BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (`employee_id`, `token`),
  FOREIGN KEY (`employee_id`) REFERENCES `Library`.`Employees` (`employee_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Library`.`calendar_notes`
-- -----------------------------------------------------
  CREATE TABLE IF NOT EXISTS `Library`.`calendar_notes` (
  `Notes_id` INT AUTO_INCREMENT NOT NULL,
  `notes_desc` varchar(255) NOT NULL,
  `Notes_date` DATE NOT NULL
  )
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Insert Data for books
-- -----------------------------------------------------
INSERT INTO Books(title, author, genre, language)
VALUES
    ('N/A', 'N/A', 'N/A', 'N/A'),
    ('The Great Adventure', 'John Smith', 'Adventure', 'English'),
    ('Mystery Mansion', 'Emily Johnson', 'Mystery', 'English'),
    ('Fantasy Quest', 'David Brown', 'Fantasy', 'English'),
    ('Science Explorers', 'John Smith', 'Science Fiction', 'English'),
    ('Romantic Escapade', 'Sophia Davis', 'Romance', 'English'),
    ('The Thriller Code', 'Michael Anderson', 'Thriller', 'English'),
    ('Historical Chronicles', 'Sarah Thompson', 'Historical Fiction', 'English'),
    ('The Comedy Club', 'Andrew Wilson', 'Comedy', 'English'),
    ('Dystopian World', 'Jennifer Adams', 'Dystopian', 'English'),
    ('Classic Tales', 'William Roberts', 'Classic', 'English'),
    ('Whodunit Mystery', 'Emily Johnson', 'Mystery', 'English'),
    ('The Magical Journey', 'Robert Harris', 'Fantasy', 'English'),
    ('Space Odyssey', 'John Smith', 'Science Fiction', 'English'),
    ('Love in Paris', 'Sophia Davis', 'Romance', 'English'),
    ('Mind Games', 'Michael Anderson', 'Thriller', 'English'),
    ('Medieval Times', 'Sarah Thompson', 'Historical Fiction', 'English'),
    ('Laugh Out Loud', 'Andrew Wilson', 'Comedy', 'English'),
    ('Post-Apocalyptic World', 'Jennifer Adams', 'Dystopian', 'English'),
    ('Literary Masterpieces', 'William Roberts', 'Classic', 'English'),
    ('Secrets Unveiled', 'Emily Johnson', 'Mystery', 'English'),
    ('Enchanted Forest', 'Robert Harris', 'Fantasy', 'English'),
    ('Alien Encounters', 'John Smith', 'Science Fiction', 'English'),
    ('Love at First Sight', 'Sophia Davis', 'Romance', 'English'),
    ('The Hidden Agenda', 'Michael Anderson', 'Thriller', 'English'),
    ('Ancient Empires', 'Sarah Thompson', 'Historical Fiction', 'English'),
    ('Funny Fiasco', 'Andrew Wilson', 'Comedy', 'English'),
    ('Survival Instincts', 'Jennifer Adams', 'Dystopian', 'English'),
    ('Literary Classics Revisited', 'William Roberts', 'Classic', 'English'),
    ('Cryptic Clues', 'Emily Johnson', 'Mystery', 'English'),
    ('Kingdom of Magic', 'Robert Harris', 'Fantasy', 'English'),
    ('Robots and Androids', 'John Smith', 'Science Fiction', 'English'),
    ('Love on the Beach', 'Sophia Davis', 'Romance', 'English'),
    ("The Mind's Eye", 'Michael Anderson', 'Thriller', 'English'),
    ('Revolutionary Times', 'Sarah Thompson', 'Historical Fiction', 'English'),
    ('Comical Capers', 'Andrew Wilson', 'Comedy', 'English'),
    ('After the Cataclysm', 'Jennifer Adams', 'Dystopian', 'English'),
    ('Literary Gems', 'William Roberts', 'Classic', 'English'),
    ('Case of the Missing Diamond', 'Emily Johnson', 'Mystery', 'English'),
    ('Wizards and Wonders', 'Robert Harris', 'Fantasy', 'English'),
    ('Interstellar Adventures', 'John Smith', 'Science Fiction', 'English'),
    ('Love in the Countryside', 'Sophia Davis', 'Romance', 'English'),
    ('The Silent Witness', 'Michael Anderson', 'Thriller', 'English'),
    ('Time Traveler Chronicles', 'Sarah Thompson', 'Historical Fiction', 'English'),
    ('Comedy Central', 'Andrew Wilson', 'Comedy', 'English'),
    ('Surviving the Apocalypse', 'Jennifer Adams', 'Dystopian', 'English'),
    ('Literary Treasures', 'William Roberts', 'Classic', 'English'),
    ('Fatal Betrayal', 'Emily Johnson', 'Mystery', 'English'),
    ('Realm of Dragons', 'Robert Harris', 'Fantasy', 'English'),
    ('Parallel Universes', 'John Smith', 'Science Fiction', 'English'),
    ('Love in the Alps', 'Sophia Davis', 'Romance', 'English'),
    ('The Dark Secret', 'Michael Anderson', 'Thriller', 'English'),
    ('Revolutionary War Chronicles', 'Sarah Thompson', 'Historical Fiction', 'English'),
    ('Laugh Riot', 'Andrew Wilson', 'Comedy', 'English'),
    ('Shakespearean Delights', 'William Roberts', 'Classic', 'English'),
    ('The Haunted Manor', 'Emily Johnson', 'Mystery', 'English'),
    ('Land of Magic', 'Robert Harris', 'Fantasy', 'English'),
    ('Exoplanetary Explorers', 'John Smith', 'Science Fiction', 'English'),
    ('Love in the Wilderness', 'Sophia Davis', 'Romance', 'English'),
    ('The Mysterious Stranger', 'Michael Anderson', 'Thriller', 'English'),
    ('Renaissance Chronicles', 'Sarah Thompson', 'Historical Fiction', 'English'),
    ('Comic Caper', 'Andrew Wilson', 'Comedy', 'English'),
    ('Beyond the Ruins', 'Jennifer Adams', 'Dystopian', 'English'),
    ('Literary Reflections', 'William Roberts', 'Classic', 'English'),
    ('The Stolen Artifact', 'Emily Johnson', 'Mystery', 'English'),
    ('Realm of Sorcery', 'Robert Harris', 'Fantasy', 'English'),
    ('Cosmic Adventures', 'John Smith', 'Science Fiction', 'English'),
    ('Love Under the Stars', 'Sophia Davis', 'Romance', 'English'),
    ('The Final Showdown', 'Jane Anderson', 'Thriller', 'English'),
    ('Lost in Time', 'Sarah Thompson', 'Historical Fiction', 'English'),
    ('Laugh-a-Palooza', 'Andrew Wilson', 'Comedy', 'English'),
    ('Apocalyptic Chronicles', 'Jennifer Adams', 'Dystopian', 'English'),
    ('Classic Adventures', 'William Roberts', 'Classic', 'English'),
    ('The Enigma Files', 'Emily Johnson', 'Mystery', 'English'),
    ('Mythical Realms', 'Robert Harris', 'Fantasy', 'English'),
    ('Galaxy Explorers', 'John Smith', 'Science Fiction', 'English'),
    ('Love in the Rain', 'Sophia Davis', 'Romance', 'English'),
    ('The Conspiracy Theory', 'Michael Anderson', 'Thriller', 'English'),
    ('Victorian Era Chronicles', 'Sarah Thompson', 'Historical Fiction', 'English'),
    ('The New World', 'Jennifer Adams', 'Dystopian', 'English'),
    ('Literary Escapades', 'William Roberts', 'Classic', 'English'),
    ('The Puzzle Master', 'Emily Johnson', 'Mystery', 'English'),
    ('Enchanted Kingdom', 'Robert Harris', 'Fantasy', 'English'),
    ('Space Odyssey II', 'John Smith', 'Science Fiction', 'English'),
    ('Love in the City', 'Sophia Davis', 'Romance', 'English'),
    ('The Dark Shadows', 'Michael Anderson', 'Thriller', 'English'),
    ('Revolutionary Tales', 'Sarah Thompson', 'Historical Fiction', 'English'),
    ('Comedy Bonanza', 'Andrew Wilson', 'Comedy', 'English'),
    ('The Last Hope', 'Jennifer Adams', 'Dystopian', 'English'),
    ('Literary Odyssey', 'William Roberts', 'Classic', 'English'),
    ('The Secret Society', 'Emily Johnson', 'Mystery', 'English'),
    ('Realm of Magic', 'Robert Harris', 'Fantasy', 'English'),
    ('Astro Adventures', 'John Smith', 'Science Fiction', 'English'),
    ('Love in the Woods', 'Sophia Davis', 'Romance', 'English'),
    ('The Betrayed', 'Michael Anderson', 'Thriller', 'English'),
    ('Medieval Tales', 'Sarah Thompson', 'Historical Fiction', 'English'),
    ('Comedy Mania', 'Andrew Wilson', 'Comedy', 'English'),
    ('The Final Countdown', 'Jennifer Adams', 'Dystopian', 'English'),
    ('Classic Revival', 'William Roberts', 'Classic', 'English'),
    ('The Secret Agent', 'Emily Johnson', 'Mystery', 'English'),
    ('Magical Realms', 'Robert Harris', 'Fantasy', 'English'),
    ('Interstellar Encounters', 'John Smith', 'Science Fiction', 'English'),
    ('Love in the City II', 'Sophia Davis', 'Romance', 'English'),
    ('The Final Revelation', 'Michael Anderson', 'Thriller', 'English'),
    ('Victorian Chronicles', 'Sarah Thompson', 'Historical Fiction', 'English');

-- -----------------------------------------------------
-- Insert Data for clients
-- -----------------------------------------------------

INSERT INTO Clients(name, surname, email, password)
VALUES
    ('N/A', '', 'N/A', 'N/A'),
    ('John', 'Doe', 'johndoe@example.com', '$2b$12$qSmGuXeUttNu5DNW9GeReeKsJCZTzOyXMM/o7i1IlEzHesxPxeNZG'),
    ('Jane', 'Smith', 'janesmith@example.com', '$2b$12$w2YDleHnws.8yM20seXTvePkuoVFcJQlPBrSn88WKkjG5s.WLjn4K'),
    ('Bob', 'Johnson', 'bobjohnson@example.com', '$2b$12$rVLaQTU.bnRgH6eS7JHGV.7RQHNwR2qfNIO4i.D1D2NC2Yfij3O1S'),
    ('Alice', 'Williams', 'alicewilliams@example.com', '$2b$12$9XIr2Eu1wW927NKaH50b3.e/OfOWEMKnotnkdyM7434Giit84H51O'),
    ('David', 'Brown', 'davidbrown@example.com', '$2b$12$LW7fTr.X1Dfy/QKC.geZt.1BUOICNwRSkQUgSK6WPFe40BJyTtv1a');

-- -----------------------------------------------------
-- Insert Data for borrowings
-- -----------------------------------------------------
INSERT INTO Borrowings(book_id, client_id, from_date, to_date, due_date)
VALUES
     (2, 6, '2022-01-01', '2022-01-15', '2022-01-08'),
    (31, 5, '2022-01-02', '2022-01-16', '2022-01-09'),
    (52, 4, '2022-01-03', '2022-01-17', '2022-01-10'),
    (100, 3, '2022-01-04', '2022-01-18', '2022-01-11'),
    (40, 6, '2022-02-01', '2022-02-15', '2022-02-08'),
    (18, 2, '2022-02-05', '2022-02-12', '2022-02-12'),
    (3, 5, '2022-03-02', '2022-03-16', '2022-03-09'),
    (43, 4, '2022-03-03', '2022-03-17', '2022-03-10'),
    (53, 3, '2022-03-04', '2022-03-18', '2022-03-11'),
    (61, 2, '2022-04-05', '2022-04-12', '2022-04-12'),
    (77, 6, '2022-05-01', '2022-05-15', '2022-05-08'),
    (31, 5, '2022-06-02', '2022-06-16', '2022-06-09'),
    (52, 4, '2022-06-03', '2022-06-17', '2022-06-10'),
    (100, 3, '2022-07-04', '2022-07-18', '2022-07-11'),
    (45, 6, '2022-08-01', '2022-08-15', '2022-08-08'),
    (16, 2, '2022-08-05', '2022-08-12', '2022-08-12'),
    (3, 5, '2022-08-02', '2022-08-16', '2022-08-09'),
    (43, 4, '2022-09-03', '2022-09-17', '2022-09-10'),
    (89, 3, '2022-09-04', '2022-09-18', '2022-09-11'),
    (44, 3, '2022-10-04', '2022-10-18', '2022-10-11'),
    (61, 2, '2022-11-05', '2022-11-12', '2022-11-12'),
    (2, 6, '2022-11-01', '2022-11-15', '2022-11-08'),
    (31, 5, '2022-12-02', '2022-12-16', '2022-12-09'),
    (52, 4, '2022-12-03', '2022-12-17', '2022-12-10'),
    (99, 3, '2023-01-04', '2023-01-18', '2023-01-11'),
    (40, 6, '2023-02-01', '2023-02-15', '2023-02-08'),
    (66, 2, '2023-03-05', '2023-03-12', '2023-03-12'),
    (3, 5, '2023-04-02', '2023-04-16', '2023-04-09'),
    (52, 4, '2023-05-03', '2023-05-17', '2023-05-10'),
    (98, 3, '2023-05-04', '2023-05-18', '2023-05-11'),
    (40, 6, '2023-05-01', '2023-05-15', '2023-05-08'),
    (16, 2, '2023-05-05', '2023-05-12', '2023-05-12'),
    (7, 5, '2023-06-02', '2023-06-16', '2023-06-09'),
    (43, 4, '2023-06-03', '2023-06-17', '2023-06-10'),
    (4, 3, '2023-06-02', Null, '2023-06-09'),
    (20, 5, '2023-06-03', '2023-06-17', '2023-06-10');


-- -----------------------------------------------------
-- Insert Data for employees
-- -----------------------------------------------------
INSERT INTO Employees(name, surname, email, password)
VALUES
    ('Keith', 'Maxwell', 'keithmaxwell@example.com', '$2b$12$g6jMYu7YN6KWf9LXbFu2debD60Zy4jkg8h0ZE0y.EnyNd2RuMTaJW'),
    ('John', 'Doe', 'johndoe@example.com', '$2b$12$azgjeFhB1bRUxGw8tEZKuecWdHn.zvCgSf.nsuS2.hNLu2aahlmle'),
    ('Jane', 'Smith', 'janesmith@example.com', '$2b$12$jrFH7utZ3rmLSPsQfZtfiOxA8pLhMVO2jEzFLTbBWh.RyenNRUnE.'),
    ('David', 'Johnson', 'davidjohnson@example.com', '$2b$12$Kbh3V7TDLSkCG2/HPIDuJ.QHEMUEOgVil5CFSWGlD3JDNo7dnk2tS'),
    ('Emily', 'Taylor', 'emilytaylor@example.com', '$2b$12$yOIoAlEts2P2rLJ0uJpzSeQ.Eg8wmbKn2K8.aroOKCZGaxug5fE42'),
    ('William', 'Brown', 'williambrown@example.com', '$2b$12$liw/eMzBs.eUN.mEHLKnqOYHp7olwOmhCHgfuGVGZ1oK8y0e2azr.'),
    ('Olivia', 'Miller', 'oliviamiller@example.com', '$2b$12$S/gMIY8bAkOKx8V3MPKqDO.ZrihqDaUyxcSRggaizVUYYUlI2nG6y'),
    ('James', 'Davis', 'jamesdavis@example.com', '$2b$12$UeknEExRxpwLSxLId4tJZOiM/AM5.Wtl0s/ZJB7ix0eNMKuAIEAES'),
    ('Ava', 'Wilson', 'avawilson@example.com', '$2b$12$gbQ3gTopXXLloosped4pBOM21CsiqQKlvHtJhzxpQ5wDm4MtJC6ky'),
    ('Michael', 'Anderson', 'michaelanderson@example.com', '$2b$12$LRewq7opm1LthH3u8rWoHugmd3nqXdAzIld4GKgmV/phTvZ3NGsgO'),
    ('Sophia', 'Thompson', 'sophiathompson@example.com', '$2b$12$LRewq7opm1LthH3u8rWoHugmd3nqXdAzIld4GKgmV/phTvZ3NGsgO'),
    ('quick', 'login', 'a', '$2b$12$Xd1PqGpiFdoab3RgISsOEefNg5yKpyBtKaa1RuchADVkUeJim6ODC'),
    ('Andrii', 'Sukhov', 'andrey.m.suhov@gmail.com', '$2b$12$xGiSBOoEmqAKQhFoYca/hOAKd/I1x7nWMXp13y6oEQkPJKkh2gsDK');

-- -----------------------------------------------------
-- Insert Data for jobs
-- -----------------------------------------------------
INSERT INTO Library.Jobs (employee_id, title, from_date, to_date)
VALUES
    (1, 'Manager', '2021-01-01', '2021-12-31'),
    (2, 'Librarian', '2022-01-01', NULL),
    (3, 'Clerk', '2022-01-01', NULL),
    (4, 'Janitor', '2021-07-01', '2022-06-30'),
    (5, 'Security Guard', '2021-01-01', '2021-12-31');

-- -----------------------------------------------------
-- create delete triggers
-- -----------------------------------------------------

delimiter #

CREATE TRIGGER change_book_references_in_borrowings
  BEFORE DELETE ON Books
  FOR EACH ROW
  BEGIN 
  UPDATE Borrowings
    SET book_id = 1
    WHERE book_id = old.book_id;

END#

CREATE TRIGGER change_client_references_in_borrowings
  BEFORE DELETE ON Clients
  FOR EACH ROW
  BEGIN 
  UPDATE Borrowings
    SET client_id = 1
    WHERE client_id = old.client_id;

END#

delimiter ;

-- -----------------------------------------------------
-- views
-- -----------------------------------------------------

CREATE VIEW available_books
AS SELECT * from books WHERE book_id not in (SELECT book_id FROM borrowings WHERE to_date is NULL);

CREATE VIEW unavailable_books
AS SELECT * from books WHERE book_id in (SELECT book_id FROM borrowings WHERE to_date is NULL);

CREATE VIEW borrowing_clients
AS SELECT * from clients WHERE client_id in (SELECT client_id FROM borrowings WHERE to_date is NULL);

CREATE VIEW non_borrowing_clients
AS SELECT * from clients WHERE client_id not in (SELECT client_id FROM borrowings WHERE to_date is NULL);

CREATE VIEW returned_books
AS SELECT * from borrowings WHERE to_date is not NULL;

CREATE VIEW borrowed_books
AS SELECT * from borrowings WHERE to_date is NULL;

CREATE VIEW overdue_books
AS SELECT * from borrowed_books WHERE due_date < curdate();





SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;