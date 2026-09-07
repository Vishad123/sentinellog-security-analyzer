import csv, json
from pathlib import Path

FIELDS = ["timestamp","service","event_type","username","ip","score","severity","description"]

def _serializable(alert):
    result = dict(alert)
    result["timestamp"] = result["timestamp"].isoformat(sep=" ")
    return result

def write_reports(alerts, directory="reports"):
    Path(directory).mkdir(exist_ok=True)
    data = [_serializable(a) for a in alerts]
    with open(Path(directory) / "alerts.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    with open(Path(directory) / "alerts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(data)

def summary(alerts):
    counts = {"CRITICAL":0,"HIGH":0,"MEDIUM":0,"LOW":0}
    for alert in alerts: counts[alert["severity"]] += 1
    return counts
