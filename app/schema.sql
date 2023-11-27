DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS kategories;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    uid INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL

);

CREATE TABLE kategories(
katID INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
color STRING NOT NULL

);

CREATE TABLE notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description INTEGER NOT NULL,
    color STRING NOT NULL
    -- katID INTEGER,
    -- FOREIGN KEY(katID)
    --         REFERENCES katergori(katID)
    -- uid INTEGER ,
    -- FOREIGN KEY(uid)
    --         REFERENCES users(uid)
);
