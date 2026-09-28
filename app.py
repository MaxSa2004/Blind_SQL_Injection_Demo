from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

DATABASE = "database.db"


def get_db():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/")
def index():
    search = request.args.get("search", "")

    connection = get_db()

    # INTENTIONALLY VULNERABLE QUERY
    query = f"""
        SELECT title, date, location
        FROM events
        WHERE title LIKE '%{search}%'
    """

    try:
        events = connection.execute(query).fetchall()
    except Exception:
        events = []

    connection.close()

    return render_template("index.html", events=events, search=search)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
