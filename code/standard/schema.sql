DROP DATABASE IF EXISTS 'stocks_database';
CREATE DATABASE stocks_database;

USE stocks_database;

DROP TABLE IF EXISTS 'securities';
CREATE TABLE securities (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  symbol VARCHAR(255),
  name VARCHAR(255),
  exchange VARCHAR(255),
  asset_type VARCHAR(255),
  sector VARCHAR(255),
  industry VARCHAR(255),
  country VARCHAR(255)
);

DROP TABLE IF EXISTS 'stocks';
CREATE TABLE stocks (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  symbol VARCHAR(255),
  name_of_stock VARCHAR(255),
  price DECIMAL(10,2),
  num_shares INT,
  total_value DECIMAL(10,2),
  purchase_price DECIMAL(10,2),
  daily_change_dollars DECIMAL(10,2),
  daily_change_percent DECIMAL(10,2),
  total_change_dollars DECIMAL(10,2),
  total_change_percent DECIMAL(10,2),
  break_even_50 VARCHAR(255),
  break_even_33 VARCHAR(255),
  break_even_25 VARCHAR(255),
  lost_50 VARCHAR(255),
  lost_66 VARCHAR(255),
  lost_75 VARCHAR(255),
  dividends DECIMAL(10,2),
  market_cap DECIMAL(10,2),
  eps DECIMAL(10,2),
  pe_ratio DECIMAL(10,2),
  sector VARCHAR(255),
  industry VARCHAR(255),
  style VARCHAR(255),
  security_id INT,
  FOREIGN KEY (security_id) REFERENCES securities(id)
);

DROP TABLE IF EXISTS 'orders';
CREATE TABLE orders (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  symbol VARCHAR(255),
  order_type VARCHAR(255),
  order_price DECIMAL(10,2),
  num_shares INT,
  order_date DATE,
  stock_id INT,
  FOREIGN KEY (stock_id) REFERENCES stocks(id)
);