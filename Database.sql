
DROP TABLE IF EXISTS tickets;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS users;

-- Now recreate the tables
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone_nr TEXT,
    password TEXT NOT NULL
);

CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    artist_name TEXT NOT NULL,
    genre TEXT,
    venue TEXT,
    date TIMESTAMP,
    price INT
    images VARCHAR(255),
);

CREATE TABLE tickets (
    ticket_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    event_id INT REFERENCES events(event_id),
    quantity INT,
    buy_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (name, email, phone_nr, password)
VALUES 
('Alice', 'alice@mail.com', '12345678', 'password123'),
('Test', 'a','123','a');
     
INSERT INTO tickets (user_id, event_id, quantity, buy_date)
VALUES (1, 1, 2, '2025-06-01 10:00');

INSERT INTO events (event_id, artist_name, genre, venue, date, price)
VALUES 
(1,'Tobias Rahim', 'Pop', 'KB Hallen', '2025-06-20 20:00', 300),
(2,'Dua Lipa', 'Pop', 'Royal Arena', '2025-06-21 21:00', 450),
(3,'The Weeknd', 'R&B', 'Parken Stadium', '2025-06-22 19:00', 600),
(4,'Metallica', 'Rock', 'Telia Parken', '2025-06-23 18:00', 700),
(5,'Adele', 'Pop', 'Copenhagen Opera House', '2025-06-24 20:00', 800),
(6,'Billie Eilish', 'Pop', 'Tivoli Concert Hall', '2025-06-25 19:30', 500),
(7,'Ed Sheeran', 'Pop', 'Royal Arena', '2025-06-26 20:00', 550),
(8,'Coldplay', 'Rock', 'Parken Stadium', '2025-06-27 21:00', 650),
(9,'Beyonce', 'R&B', 'Copenhagen Opera House', '2025-06-28 20:00', 900),
(10,'Drake', 'Hip-Hop', 'Telia Parken', '2025-06-29 19:00', 700),
(11,'Taylor Swift', 'Pop', 'Royal Arena', '2025-06-30 20:00', 750),
(13,'Medina', 'Pop', 'KB Hallen', '2025-07-01 20:00', 400),
(14,'Rammstein', 'Metal', 'Parken Stadium', '2025-07-02 19:00', 800),
(15,'Imagine Dragons', 'Rock', 'Copenhagen Opera House', '2025-07-03 20:00', 600),
(16,'Post Malone', 'Hip-Hop', 'Tivoli Concert Hall', '2025-07-04 21:00', 500),
(17,'Simon Kvamm', 'Pop', 'KB Hallen', '2025-07-05 20:00', 350),
(18,'Hozier', 'Indie', 'Royal Arena', '2025-07-06 19:30', 400),
(19,'Lars Lilholt Band', 'Folk', 'Telia Parken', '2025-07-07 20:00', 300),
(20,'Kashmir', 'Rock', 'Parken Stadium', '2025-07-09 19:00', 500);

UPDATE events SET images = 'Tobias Rahim.png' WHERE artist_name = 'Tobias Rahim';
UPDATE events SET images = 'Dua Lipa.png' WHERE artist_name = 'Dua Lipa';


select * from events;

