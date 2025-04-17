import sqlite3
import os

os.makedirs('db', exist_ok=True)
db_path = os.path.join('db', 'workouts.db')
conn = sqlite3.connect(db_path)

with open('db/schema.sql') as f:
    conn.executescript(f.read())

# Seed exercises
data = [
    ('legs', 'Squats', 3, 10),
    ('legs', 'Lunges', 3, 12),
    ('chest', 'Bench Press', 3, 10),
    ('arms', 'Bicep Curls', 2, 15),
    ('cardio', 'Running', 1, 30)
]
conn.executemany("INSERT INTO exercises (type, name, sets, reps) VALUES (?, ?, ?, ?)", data)

conn.commit()
conn.close()
print("Database initialized and seeded!")