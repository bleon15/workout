import sqlite3
import os

# Set up database path
os.makedirs('db', exist_ok=True)
db_path = os.path.join('db', 'workouts.db')
conn = sqlite3.connect(db_path)

# Execute schema.sql to create tables
with open('db/schema.sql') as f:
    conn.executescript(f.read())

# Seed exercises with 'miles' as NULL where it's not applicable
data = [
    ('legs', 'Squats', 3, 10, None),
    ('legs', 'Lunges', 3, 12, None),
    ('chest', 'Bench Press', 3, 10, None),
    ('arms', 'Bicep Curls', 2, 15, None),
    ('cardio', 'Running', None, None, 2)  # For cardio, use 'miles'
]

# Insert data into the exercises table (with correct number of columns)
conn.executemany("INSERT INTO exercises (type, name, sets, reps, miles) VALUES (?, ?, ?, ?, ?)", data)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database initialized and seeded!")