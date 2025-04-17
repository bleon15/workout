import sqlite3
import os
from flask import app, render_template
import pandas as pd

from app import app, get_weekly_workout_count 

os.makedirs('db', exist_ok=True)
db_path = os.path.join('db', 'workouts.db')
conn = sqlite3.connect(db_path)

with open('db/schema.sql') as f:
    conn.executescript(f.read())

# Load preprocessed dataset
csv_path = 'db/Workout.csv'
df = pd.read_csv(csv_path)

# Normalize values
df["Sets"] = df["Sets"].astype(str).str.extract(r"(\d+)").fillna(0).astype(int)
df["Reps"] = df["Reps"].astype(str).str.extract(r"(\d+)").fillna(0).astype(int)

# Insert into DB
for _, row in df.iterrows():
    conn.execute(
    "INSERT INTO exercises (Category, Workout, Sets, Reps) VALUES (?, ?, ?, ?)",
    (row['Category'], row['Workout'], row['Sets'], row['Reps'])
)


conn.commit()
conn.close()
print("Database initialized and seeded from Workout.csv!")


