from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), 'db', 'workouts.db')


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return render_template('index.html', workouts_completed=3)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/workouts')
def workout_selection():
    return render_template('workout_selection.html')


@app.route('/workouts/<workout_type>')
def workout_details(workout_type):
    conn = get_db()
    cursor = conn.execute("SELECT name, sets, reps FROM exercises WHERE type = ?", (workout_type,))
    exercises = cursor.fetchall()
    conn.close()
    return render_template('workout_details.html', workout_name=f"{workout_type.title()} Day", exercises=exercises)


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
