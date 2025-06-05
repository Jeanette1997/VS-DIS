-- SQLite
DROP TABLE IF EXISTS tickets;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS users;

-- Now recreate the tables
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone_nr TEXT
);

CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    artist_name TEXT NOT NULL,
    genre TEXT,
    venue TEXT,
    date TIMESTAMP,
    price INT
);

CREATE TABLE tickets (
    ticket_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    event_id INT REFERENCES events(event_id),
    quantity INT,
    buy_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (name, email, phone_nr)
VALUES ('Alice', 'alice@mail.com', '12345678');

INSERT INTO events (artist_name, genre, venue, date, price)
VALUES 
('Tobias Rahim', 'Pop', 'KB Hallen', '2025-06-20 20:00', 300),
('Dua Lipa', 'Pop', 'Royal Arena', '2025-06-21 21:00', 450);


select * from events;

