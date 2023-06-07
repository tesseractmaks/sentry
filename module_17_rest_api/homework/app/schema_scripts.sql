PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS 'author';
CREATE TABLE 'author' (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50) NOT NULL
);


DROP TABLE IF EXISTS 'books';
CREATE TABLE 'books' (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    author INTEGER NOT NULL REFERENCES author(author_id) ON DELETE CASCADE,
    book_name VARCHAR(100) NOT NULL
);




