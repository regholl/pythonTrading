DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS securities;
DROP TABLE IF EXISTS positions;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS portfolios;
DROP TABLE IF EXISTS experiments;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);


CREATE TABLE securities (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  symbol TEXT NOT NULL,
  security_type TEXT NOT NULL,
  currency TEXT NOT NULL
);

CREATE TABLE positions (
  id INTEGER PRIMARY KEY,
  security_id INTEGER NOT NULL,
  account_id INTEGER NOT NULL,
  quantity INTEGER NOT NULL,
  average_price REAL NOT NULL,
  FOREIGN KEY (security_id) REFERENCES securities (id),
  FOREIGN KEY (account_id) REFERENCES accounts (id)
);

CREATE TABLE orders (
  id INTEGER PRIMARY KEY,
  security_id INTEGER NOT NULL,
  account_id INTEGER NOT NULL,
  order_type TEXT NOT NULL,
  order_status TEXT NOT NULL,
  quantity INTEGER NOT NULL,
  price REAL NOT NULL,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  FOREIGN KEY (security_id) REFERENCES securities (id),
  FOREIGN KEY (account_id) REFERENCES accounts (id)
);

CREATE TABLE experiments (
  id INTEGER PRIMARY KEY,
  portfolio_id INTEGER NOT NULL,
  FOREIGN KEY (portfolio_id) REFERENCES portfolios (id)
);
