Описать таблицу фильм: id, название, длительность,
режиссер, жанр фильма. Обратите внимание на то,
что у фильма может быть более одного жанра, а к
одному жанру может относится более, чем один
фильм.

CREATE TABLE films
(
    film_id INT PRIMARY KEY ,
    film_name varchar(128) not null ,
    film_long int not null ,
    film_prod varchar(128)
);

INSERT INTO films(film_id, film_name, film_long, film_prod) VALUES (1, 'Harry Potter', 220, 'Garry Hua');
INSERT INTO films(film_id, film_name, film_long, film_prod) VALUES (2, 'RAMBO 2', 180, 'Mary Hua');
INSERT INTO films(film_id, film_name, film_long, film_prod) VALUES (3, 'Kik the pick', 440, 'Jonny Week');
INSERT INTO films(film_id, film_name, film_long, film_prod) VALUES (4, 'Only Alone', 150, 'Marty Robinson');


CREATE TABLE category
(
    category_id INT PRIMARY KEY ,
    category_name varchar(128) not null
);

INSERT INTO category(category_id, category_name) VALUES (1, 'Comedy');
INSERT INTO category(category_id, category_name) VALUES (2, 'Fight');
INSERT INTO category(category_id, category_name) VALUES (3, 'Document Film');
INSERT INTO category(category_id, category_name) VALUES (4, 'Horror');

CREATE TABLE FilmCategory
(
    film_id     INT,
    category_id INT,
    primary key (category_id, film_id),
    CONSTRAINT fk_films
    FOREIGN KEY (film_id)
    REFERENCES films(film_id)
    ON DELETE CASCADE ,
    CONSTRAINT fk_category
    FOREIGN KEY (category_id)
    REFERENCES category(category_id)
    ON DELETE CASCADE
);

INSERT INTO FilmCategory(film_id, category_id) VALUES (1, 4);
INSERT INTO FilmCategory(film_id, category_id) VALUES (1, 2);
INSERT INTO FilmCategory(film_id, category_id) VALUES (2, 1);
INSERT INTO FilmCategory(film_id, category_id) VALUES (2, 2);
INSERT INTO FilmCategory(film_id, category_id) VALUES (3, 3);
INSERT INTO FilmCategory(film_id, category_id) VALUES (4, 2);
INSERT INTO FilmCategory(film_id, category_id) VALUES (4, 4);

SELECT film_name, category_name FROM films
INNER JOIN FilmCategory ON films.film_id = FilmCategory.film_id
INNER JOIN category c on FilmCategory.category_id = c.category_id


Описать таблицу песня: id, название, длительность,
певец. При этом у песни может быть более одного
певца, а певец мог записать более одной песни.

CREATE TABLE song
(
    song_id int primary key ,
    song_name varchar(128) not null ,
    song_long int not null
);


INSERT INTO song(song_id, song_name, song_long) VALUES (1, 'Luxe', 3.40);
INSERT INTO song(song_id, song_name, song_long) VALUES (2, 'Weather Sun', 1.60);
INSERT INTO song(song_id, song_name, song_long) VALUES (3, 'Pick me up', 2.40);
INSERT INTO song(song_id, song_name, song_long) VALUES (4, 'Hit the Roll, Jack', 1.30);

CREATE TABLE artist
(
    artist_id int primary key ,
    artist_name varchar(128) not null
);

INSERT INTO artist(artist_id, artist_name) VALUES (1, 'Mike WIll');
INSERT INTO artist(artist_id, artist_name) VALUES (2, 'Killo Jumba');
INSERT INTO artist(artist_id, artist_name) VALUES (3, 'Ama Band');


CREATE TABLE SongArtist
(
    song_id int ,
    artist_id int,
    CONSTRAINT fk_song
    FOREIGN KEY (song_id)
    REFERENCES song(song_id)
    ON DELETE CASCADE ,
    CONSTRAINT fk_artist
    FOREIGN KEY (artist_id)
    REFERENCES artist(artist_id)
    ON DELETE CASCADE
);

INSERT INTO SongArtist(song_id, artist_id) VALUES (1, 1);
INSERT INTO SongArtist(song_id, artist_id) VALUES (1, 3);
INSERT INTO SongArtist(song_id, artist_id) VALUES (2, 2);
INSERT INTO SongArtist(song_id, artist_id) VALUES (3, 1);
INSERT INTO SongArtist(song_id, artist_id) VALUES (3, 2);


SELECT song_name, artist_name FROM song
INNER JOIN SongArtist SA on song.song_id = SA.song_id
INNER JOIN artist a on a.artist_id = SA.artist_id


Реализовать таблицу машина: модель,
производитель, цвет, цена.

Описать отдельную таблицу производитель: id,
название, рейтинг.
Описать отдельную таблицу цвета: id, название.
У одной машины может быть только один
производитель, а у производителя  много машин. У
одной машины может быть много цветов, а у одного
цвета может быть много машин.

CREATE TABLE Generic
(
    generic_id int primary key ,
    generic_name varchar(128) not null ,
    generic_rank int not null
);

INSERT INTO Generic(generic_id, generic_name, generic_rank) VALUES (1, 'Audi', 9);
INSERT INTO Generic(generic_id, generic_name, generic_rank) VALUES (2, 'BWM', 7);
INSERT INTO Generic(generic_id, generic_name, generic_rank) VALUES (3, 'Mercedes', 9);

CREATE TABLE Car
(
    car_id int primary key ,
    car_model varchar(128) not null ,
    generic_id int ,
    color_id int ,
    car_price int not null,
    CONSTRAINT fk_generic
    FOREIGN KEY (generic_id)
    REFERENCES Generic(generic_id)
    ON DELETE CASCADE,
    CONSTRAINT fk_color
    FOREIGN KEY (color_id)
    REFERENCES Color(color_id)
    ON DELETE CASCADE
);

INSERT INTO Car(car_id, car_model, generic_id, color_id, car_price) VALUES (1, 'A4', 1, 1, 15000);
INSERT INTO Car(car_id, car_model, generic_id, color_id, car_price) VALUES (2, 'A6', 1, 2, 20000);
INSERT INTO Car(car_id, car_model, generic_id, color_id, car_price) VALUES (3, 'M5', 2, 3, 25000);
INSERT INTO Car(car_id, car_model, generic_id, color_id, car_price) VALUES (4, 'X6', 2, 1, 22000);
INSERT INTO Car(car_id, car_model, generic_id, color_id, car_price) VALUES (5, 'E212', 3, 2, 15000);
INSERT INTO Car(car_id, car_model, generic_id, color_id, car_price) VALUES (6, 'G63', 3, 4, 70000);

CREATE TABLE Color
(
    color_id int primary key ,
    color_name varchar(128) not null
);

INSERT INTO Color(color_id, color_name) VALUES (1, 'Black');
INSERT INTO Color(color_id, color_name) VALUES (2, 'White');
INSERT INTO Color(color_id, color_name) VALUES (3, 'Green');
INSERT INTO Color(color_id, color_name) VALUES (4, 'Red');


CREATE TABLE CarColor
(
    car_id int,
    color_id int,
    primary key (car_id, color_id),
    CONSTRAINT fk_car
    FOREIGN KEY (car_id)
    REFERENCES Car(car_id)
    ON DELETE CASCADE ,
    CONSTRAINT fk_color
    FOREIGN KEY (color_id)
    REFERENCES Color(color_id)
    ON DELETE CASCADE
);

SELECT generic_name, car_model, color_name, car_price FROM Generic
INNER JOIN car c on Generic.generic_id = c.generic_id
INNER JOIN Color C2 on C2.color_id = c.color_id