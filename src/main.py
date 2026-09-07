import argparse
from .analyzer import analyze

def main():
    parser = argparse.ArgumentParser(description="Analyze synthetic authentication logs defensively.")
    parser.add_argument("--log", required=True, help="Path to an authorized/synthetic log file")
    args = parser.parse_args()
    events, alerts, counts = analyze(args.log)
    print("=" * 44)
    print("SENTINELLOG SECURITY REPORT")
    print("=" * 44)
    print(f"Events analyzed : {len(events)}")
    print(f"Alerts generated: {len(alerts)}")
    for level in ("CRITICAL","HIGH","MEDIUM","LOW"):
        print(f"{level:9}: {counts[level]}")
    print("Reports: reports/alerts.csv and reports/alerts.json")

if __name__ == "__main__":
    main()
