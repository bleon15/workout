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
    ('legs', 'Goblin Squats', 3, 10),
    ('chest', 'Bench Press', 3, 10),
    ('chest', 'Chest Fly', 3, 12),
    ('chest', 'Incline Dumbell Press', 4, 8),
    ('arms', 'Bicep Curls', 2, 15),
    ('arms', 'Hammer Curls', 2, 15),
    ('arms', 'Preacher Curls', 2, 15),
    ('cardio', 'Running', 1, 30)
    ('cardio', 'Sprints', 5, 10)
]
conn.executemany("INSERT INTO exercises (type, name, sets, reps) VALUES (?, ?, ?, ?)", data)

conn.commit()
conn.close()
print("Database initialized and seeded!")
