CREATE TABLE IF NOT EXISTS exercises (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Category TEXT NOT NULL,
    Workout TEXT NOT NULL,
    Sets INTEGER,
    Reps INTEGER
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

CREATE TABLE IF NOT EXISTS workout_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Category TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
