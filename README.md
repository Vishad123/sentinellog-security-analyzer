# 🛡️ SentinelLog — Security Log Analyzer

SentinelLog is a Python-based defensive security tool that analyzes authentication logs and detects suspicious login activity.

## 🎯 Project Objective

The goal of SentinelLog is to demonstrate basic Security Operations Center (SOC) concepts using Python, including:

- Authentication log analysis
- Suspicious activity detection
- Severity classification
- Security alert generation
- SQLite data storage
- CSV and JSON reporting
- Web-based security dashboard

## 🔍 Detection Capabilities

SentinelLog currently detects:

- Repeated failed login attempts
- Multiple-account targeting from an IP address
- Successful login after repeated failures
- Login activity outside configured normal hours

## 🏗️ Project Structure

```text
sentinellog-security-analyzer/
├── src/
│   ├── analyzer.py
│   ├── app.py
│   ├── config.py
│   ├── database.py
│   ├── detector.py
│   ├── main.py
│   ├── parser.py
│   └── reporter.py
├── sample_logs/
│   └── auth.log
├── templates/
│   └── dashboard.html
├── tests/
│   ├── test_detector.py
│   └── test_parser.py
├── reports/
├── requirements.txt
├── README.md
└── LICENSE
