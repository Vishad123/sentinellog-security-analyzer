import re
from datetime import datetime

LOG_PATTERN = re.compile(
    r"^(?P<timestamp>\S+\s+\S+)\s+(?P<service>\S+)\s+"
    r"(?P<event>login\s+(?:failed|success))\s+"
    r"user=(?P<username>\S+)\s+ip=(?P<ip>\S+)$"
)
EVENT_MAP = {"login failed": "login_failed", "login success": "login_success"}

def parse_line(line: str) -> dict:
    match = LOG_PATTERN.match(line.strip())
    if not match:
        raise ValueError(f"Unsupported log format: {line.strip()}")
    data = match.groupdict()
    return {
        "timestamp": datetime.strptime(data["timestamp"], "%Y-%m-%d %H:%M:%S"),
        "service": data["service"],
        "event_type": EVENT_MAP[data["event"]],
        "username": data["username"],
        "ip": data["ip"],
    }

def parse_file(path: str) -> list[dict]:
    events = []
    with open(path, "r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                events.append(parse_line(line))
            except ValueError as exc:
                raise ValueError(f"Line {line_number}: {exc}") from exc
    return events
