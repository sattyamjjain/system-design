-- Create a table and shard it by columns
CREATE TABLE mytable (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    age INTEGER,
    country TEXT
);
-- Create shards for each column
CREATE TABLE mytable_id (
    id SERIAL PRIMARY KEY,
    name TEXT
);
CREATE TABLE mytable_email (
    id SERIAL PRIMARY KEY,
    email TEXT
);
CREATE TABLE mytable_age (
    id SERIAL PRIMARY KEY,
    age INTEGER
);
CREATE TABLE mytable_country (
    id SERIAL PRIMARY KEY,
    country TEXT
);