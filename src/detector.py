from collections import defaultdict
from datetime import timedelta
from .config import Config

def severity_for_score(score: int) -> str:
    if score >= 12: return "CRITICAL"
    if score >= 8: return "HIGH"
    if score >= 4: return "MEDIUM"
    return "LOW"

def detect(events: list[dict], config: Config | None = None) -> list[dict]:
    config = config or Config()
    ordered = sorted(events, key=lambda e: e["timestamp"])
    failures_by_ip = defaultdict(list)
    alerts = []

    for event in ordered:
        ip = event["ip"]
        if event["event_type"] == "login_failed":
            failures_by_ip[ip].append(event)
            cutoff = event["timestamp"] - timedelta(minutes=config.failure_window_minutes)
            recent = [e for e in failures_by_ip[ip] if e["timestamp"] >= cutoff]
            users = {e["username"] for e in recent}
            score, reasons = 0, []

            if len(recent) >= config.failure_threshold:
                score += len(recent) * config.failure_score
                reasons.append(f"{len(recent)} failed logins within {config.failure_window_minutes} minutes")
            if len(users) >= config.multi_user_threshold:
                score += config.multi_user_score
                reasons.append(f"activity targeting {len(users)} usernames")
            if not (config.normal_start_hour <= event["timestamp"].hour < config.normal_end_hour):
                score += config.unusual_hour_score
                reasons.append("activity outside configured normal hours")

            if score:
                alerts.append({**event, "score": score,
                               "severity": severity_for_score(score),
                               "description": "; ".join(reasons)})

        elif event["event_type"] == "login_success":
            cutoff = event["timestamp"] - timedelta(minutes=config.success_after_failure_window_minutes)
            recent = [e for e in failures_by_ip[ip]
                      if cutoff <= e["timestamp"] <= event["timestamp"]]
            if len(recent) >= config.failure_threshold:
                score = len(recent) * config.failure_score + config.success_after_failure_score
                alerts.append({**event, "score": score,
                               "severity": severity_for_score(score),
                               "description": f"successful login after {len(recent)} recent failures"})
    return alerts
