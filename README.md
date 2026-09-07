# SentinelLog — Security Log Analyzer

SentinelLog is an original defensive cybersecurity portfolio project for analyzing synthetic authentication logs, detecting suspicious activity, assigning configurable severity scores, storing alerts in SQLite, and generating CSV/JSON reports.

## Features
- Authentication log parsing
- Repeated failed-login detection
- Multiple-account targeting detection
- Successful-login-after-failures detection
- Configurable unusual-hours detection
- Configurable severity scoring
- SQLite storage
- CSV and JSON reports
- Flask dashboard
- Unit tests

## Mac quick start
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m src.main --log sample_logs/auth.log
python3 -m unittest discover -s tests -v
python3 -m src.app
```
Then open http://127.0.0.1:5000.

## Safety
All included logs are synthetic. Use the analyzer only with data you own or are authorized to analyze. This project is defensive and does not perform exploitation or credential attacks.

## Portfolio note
Be prepared to explain the parser, detection rules, scoring model, database design, tests, false-positive limitations, and future improvements.
