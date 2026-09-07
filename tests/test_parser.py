import unittest
from datetime import datetime
from src.parser import parse_line

class ParserTests(unittest.TestCase):
    def test_parse_line(self):
        event = parse_line("2026-09-01 09:12:10 ssh login failed user=alice ip=192.168.1.20")
        self.assertEqual(event["event_type"], "login_failed")
        self.assertEqual(event["username"], "alice")
        self.assertEqual(event["ip"], "192.168.1.20")
        self.assertEqual(event["timestamp"], datetime(2026,9,1,9,12,10))

if __name__ == "__main__": unittest.main()
