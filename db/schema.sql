CREATE TABLE IF NOT EXISTS exercises (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    name TEXT NOT NULL,
    sets INTEGER,
    reps INTEGER,
    miles INTEGER
);

CREATE TABLE IF NOT EXISTS progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    starting_weight INTEGER,
    current_weight INTEGER,
    goal INTEGER,
    bench_press INTEGER,
    squat INTEGER,
    calories_burned INTEGER
);