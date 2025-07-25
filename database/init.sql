CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    income REAL,
    location TEXT
);

CREATE TABLE IF NOT EXISTS offers (
    offer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    category TEXT,
    discount REAL,
    message TEXT
);

CREATE TABLE IF NOT EXISTS interactions (
    interaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    offer_id INTEGER,
    channel TEXT,
    time_of_day TEXT,
    clicked BOOLEAN,
    purchased BOOLEAN,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(offer_id) REFERENCES offers(offer_id)
);
