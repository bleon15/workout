from flask import Flask, render_template, request, redirect, jsonify
from datetime import datetime, timedelta
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), 'db', 'workouts.db')


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def get_weekly_workout_count():
    conn = get_db()
    result = conn.execute("""
        SELECT COUNT(*) FROM workout_log 
        WHERE strftime('%W', timestamp) = strftime('%W', 'now')
    """).fetchone()[0]
    conn.close()
    return result


@app.route('/')
def index():
    conn = get_db()
    count = conn.execute("""
        SELECT COUNT(*) FROM workout_log 
        WHERE strftime('%W', timestamp) = strftime('%W', 'now')
    """).fetchone()[0]
    conn.close()

    return render_template('index.html', workouts_completed=count)




@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/workouts')
def workout_selection():
    return render_template('workout_selection.html')


@app.route('/workouts/<workout_type>', methods=['GET', 'POST'])
def workout_details(workout_type):
    conn = get_db()
    logged = False

    # Fetch the exercises first
    cursor = conn.execute(
    "SELECT Workout, Sets, Reps FROM exercises WHERE Category = ? ORDER BY RANDOM() LIMIT 3",
    (workout_type.title(),)
    )

    exercises = cursor.fetchall()

    if request.method == 'POST':
        # Step 1: Insert workout_log row
        conn.execute("INSERT INTO  workout_log (type) VALUES (?)", (workout_type,))
        log_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

        # Step 2: For each exercise, log how many sets were completed
        for exercise in exercises:
            name = exercise['Workout']
            sets_completed = request.form.get(f"set_{name}", 0)
            conn.execute(
                "INSERT INTO workout_log_detail (log_id, exercise, sets_completed) VALUES (?, ?, ?)",
                (log_id, name, sets_completed)
            )

        conn.commit()
        logged = True

    conn.close()
    return render_template('workout_details.html',
                           workout_name=f"{workout_type.title()} Day",
                           exercises=exercises,
                           logged=logged)




@app.route('/progress', methods=['GET', 'POST'])
def progress_tracking():
    if request.method == 'POST':
        form = request.form
        conn = get_db()
        conn.execute(
            "INSERT INTO progress (starting_weight, current_weight, goal, bench_press, squat, calories_burned) VALUES (?, ?, ?, ?, ?, ?)",
            (form['starting_weight'], form['current_weight'], form['goal'], form['bench_press'], form['squat'], form['calories_burned'])
        )
        conn.commit()
        conn.close()
        return redirect('/progress')

    conn = get_db()
    cursor = conn.execute("SELECT * FROM progress ORDER BY id DESC LIMIT 1")
    user = cursor.fetchone()
    conn.close()
    return render_template('progress_tracking.html', user=user)


@app.route('/api/progress')
def api_progress():
    conn = get_db()
    cursor = conn.execute("SELECT id, current_weight FROM progress ORDER BY id DESC LIMIT 10")
    data = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify({"data": data})


if __name__ == '__main__':
    app.run(debug=True)
