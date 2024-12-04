CREATE TABLE todo (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    description VARCHAR(500),
    done BOOLEAN DEFAULT FALSE,
    due_on INTEGER  -- Stores date as proleptic Gregorian ordinal
);