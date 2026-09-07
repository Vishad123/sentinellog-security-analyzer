from pathlib import Path

from flask import Flask, render_template

from .database import initialize, recent_alerts

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / "templates"

app = Flask(__name__, template_folder=str(TEMPLATE_DIR))


@app.route("/")
def dashboard():
    conn = initialize()
    rows = recent_alerts(conn)
    conn.close()

    counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}

    for row in rows:
        counts[row[5]] = counts.get(row[5], 0) + 1

    return render_template("dashboard.html", alerts=rows, counts=counts)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)