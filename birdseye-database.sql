DROP SCHEMA IF EXISTS birdseye;

CREATE SCHEMA birdseye CHARACTER SET utf8 COLLATE utf8_general_ci;

DROP TABLE IF EXISTS birdseye.sensors;
DROP TABLE IF EXISTS birdseye.lots;

CREATE TABLE birdseye.lots (
  lot_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL,
  description TEXT,
  location TEXT,
  spaces_available INT NOT NULL DEFAULT 0,
  total_spaces INT NOT NULL,
  active BOOL NOT NULL DEFAULT 1,
  created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (lot_id)
);

CREATE TABLE birdseye.sensors (
  sensor_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL,
  description TEXT,
  lot_id INT UNSIGNED NOT NULL,
  location TEXT,
  active BOOL NOT NULL DEFAULT 1,
  created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (sensor_id),
  FOREIGN KEY (lot_id) REFERENCES lots(lot_id)
);
