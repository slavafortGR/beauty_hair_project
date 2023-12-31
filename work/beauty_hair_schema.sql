-- MySQL Script generated by MySQL Workbench
-- Thu Nov 16 02:01:20 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema beauty_hair
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema beauty_hair
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `beauty_hair` DEFAULT CHARACTER SET utf8 ;
USE `beauty_hair` ;

-- -----------------------------------------------------
-- Table `beauty_hair`.`clients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `beauty_hair`.`clients` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `gender` VARCHAR(1) NOT NULL,
  `registration_date` DATETIME NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `beauty_hair`.`contacts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `beauty_hair`.`contacts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `client_id` INT NOT NULL,
  `value` VARCHAR(160) NOT NULL,
  `type` INT NOT NULL COMMENT 'types:\n0 - phone\n1 - telegram\n2 - viber\n3 - whatsapp\n4 - instagram\n5 - facebook\n',
  `primary` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  INDEX `client_id_idx` (`client_id` ASC) VISIBLE,
  UNIQUE INDEX `value_UNIQUE` (`value` ASC) VISIBLE,
  CONSTRAINT `client_id`
    FOREIGN KEY (`client_id`)
    REFERENCES `beauty_hair`.`clients` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `beauty_hair`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `beauty_hair`.`orders` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `client_id` INT NOT NULL,
  `start_time` DATETIME NULL,
  `end_time` DATETIME NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `client_id`
    FOREIGN KEY (`id`)
    REFERENCES `beauty_hair`.`clients` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = DEFAULT;


-- -----------------------------------------------------
-- Table `beauty_hair`.`goods`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `beauty_hair`.`goods` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(128) NOT NULL,
  `price` FLOAT NOT NULL,
  `type` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `beauty_hair`.`incomes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `beauty_hair`.`incomes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `goods_id` INT NOT NULL,
  `amount` INT NOT NULL DEFAULT 1,
  `order_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `goods_id_idx` (`goods_id` ASC) VISIBLE,
  INDEX `order_id_idx` (`order_id` ASC) VISIBLE,
  CONSTRAINT `goods_id`
    FOREIGN KEY (`goods_id`)
    REFERENCES `beauty_hair`.`goods` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `order_id`
    FOREIGN KEY (`order_id`)
    REFERENCES `beauty_hair`.`orders` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `beauty_hair`.`expenses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `beauty_hair`.`expenses` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `business_tax` FLOAT NOT NULL,
  `rent` FLOAT NOT NULL,
  `advertising` FLOAT NOT NULL,
  `buying_cosmetics` FLOAT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `beauty_hair`.`store`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `beauty_hair`.`store` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `good_id` INT NOT NULL,
  `amount` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `good_id_idx` (`good_id` ASC) VISIBLE,
  CONSTRAINT `good_id`
    FOREIGN KEY (`good_id`)
    REFERENCES `beauty_hair`.`goods` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
