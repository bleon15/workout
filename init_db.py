import sqlite3
import os

os.makedirs('db', exist_ok=True)
db_path = os.path.join('db', 'workouts.db')
conn = sqlite3.connect(db_path)

with open('db/schema.sql') as f:
    conn.executescript(f.read())

# Seed exercises
data = [
    ('legs', 'Squats', 3, 10, None),
    ('legs', 'Lunges', 3, 12, None),
    ('legs', 'Goblin Squats', 3, 10, None),
    ('chest', 'Bench Press', 3, 10, None),
    ('chest', 'Chest Fly', 3, 12, None),
    ('chest', 'Incline Dumbell Press', 4, 8, None),
    ('arms', 'Bicep Curls', 2, 15, None),
    ('arms', 'Hammer Curls', 2, 15, None),
    ('arms', 'Preacher Curls', 2, 15, None),
    ('cardio', 'Running', None, None, 3)
    ('cardio', 'Sprints', 5, 10)
]

# Insert data into the exercises table (with correct number of columns)
conn.executemany("INSERT INTO exercises (type, name, sets, reps, miles) VALUES (?, ?, ?, ?, ?)", data)

# Commit changes and close the connection
conn.commit()
conn.close()
print("Database initialized and seeded!")
