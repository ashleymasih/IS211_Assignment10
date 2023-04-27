CREATE TABLE Artist (
  artist_id INTEGER PRIMARY KEY,
  arist_Name VARCHAR(255) NOT NULL
);

CREATE TABLE Album (
  album_id INTEGER PRIMARY KEY,
  album_title VARCHAR(255) NOT NULL,
  artist_id INTEGER NOT NULL,
  FOREIGN KEY (artist_id) REFERENCES Artist(artist_id)
);

CREATE TABLE Song (
  song_id INTEGER PRIMARY KEY,
  song_title VARCHAR(255) NOT NULL,
  album_id INTEGER NOT NULL,
  track_number INTEGER NOT NULL,
  duration INTEGER NOT NULL,
  FOREIGN KEY (album_id) REFERENCES Album(album_id)
);
