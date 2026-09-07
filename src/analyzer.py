from .config import Config
from .database import initialize, insert_alerts
from .detector import detect
from .parser import parse_file
from .reporter import summary, write_reports

def analyze(log_path, db_path="sentinellog.db"):
    events = parse_file(log_path)
    alerts = detect(events, Config())
    conn = initialize(db_path)
    insert_alerts(conn, alerts)
    conn.close()
    write_reports(alerts)
    return events, alerts, summary(alerts)
