import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    service TEXT NOT NULL,
    event_type TEXT NOT NULL,
    username TEXT NOT NULL,
    ip TEXT NOT NULL,
    severity TEXT NOT NULL,
    score INTEGER NOT NULL,
    description TEXT NOT NULL
)
"""

def initialize(path="sentinellog.db"):
    conn = sqlite3.connect(path)
    conn.execute(SCHEMA)
    conn.commit()
    return conn

def insert_alerts(conn, alerts):
    conn.executemany(
        """INSERT INTO alerts
        (timestamp, service, event_type, username, ip, severity, score, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        [(a["timestamp"].isoformat(sep=" "), a["service"], a["event_type"],
          a["username"], a["ip"], a["severity"], a["score"], a["description"])
         for a in alerts])
    conn.commit()

def recent_alerts(conn, limit=100):
    return conn.execute(
        "SELECT timestamp, service, event_type, username, ip, severity, score, description "
        "FROM alerts ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
