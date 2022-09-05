CREATE TABLE IF NOT EXISTS trucks (
    id INTEGER NOT NULL,
    name VARCHAR,
    postCode VARCHAR,
    phone VARCHAR,
    country VARCHAR,
    county VARCHAR,
    long VARCHAR,
    lat VARCHAR,
    hasSpecialCharacters BOOLEAN,
    noSpecialCharacters VARCHAR,
    PRIMARY KEY (id)
);