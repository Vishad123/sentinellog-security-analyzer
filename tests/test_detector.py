import unittest
from datetime import datetime, timedelta
from src.config import Config
from src.detector import detect

def event(minutes, event_type="login_failed", user="admin"):
    return {"timestamp": datetime(2026,9,1,9,0,0)+timedelta(minutes=minutes),
            "service":"ssh","event_type":event_type,"username":user,"ip":"192.168.1.50"}

class DetectorTests(unittest.TestCase):
    def test_repeated_failures_generate_alert(self):
        alerts = detect([event(i) for i in range(5)], Config(failure_threshold=5))
        self.assertTrue(alerts)

    def test_success_after_failures(self):
        events = [event(i) for i in range(5)] + [event(6, "login_success")]
        alerts = detect(events, Config(failure_threshold=5))
        self.assertTrue(any("successful login" in a["description"] for a in alerts))

if __name__ == "__main__": unittest.main()
