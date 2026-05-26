# Day 1 - My First Security Tool
# Simple Log Analyser
# Author: Chennakeshavulu
# Date: May 26, 2026
# Goal: Detect suspicious IPs like Cloudflare WAF

log_entries = [
    {"ip": "192.168.1.1", "requests": 50},
    {"ip": "10.0.0.5",    "requests": 5000},
    {"ip": "203.0.113.7", "requests": 9999},
    {"ip": "198.51.0.2",  "requests": 25},
]

print("=" * 40)
print("   SECURITY LOG ANALYSER - DAY 1")
print("=" * 40)

suspicious = []

for entry in log_entries:
    if entry["requests"] > 1000:
        suspicious.append(entry["ip"])
        print(f" ALERT: {entry['ip']} made {entry['requests']} requests!")
    else:
        print(f" SAFE:  {entry['ip']} made {entry['requests']} requests")

print()
print(f"Total suspicious IPs: {len(suspicious)}")
print(f"Block these IPs: {suspicious}")
print()
print("This is how Cloudflare WAF detects attack traffic!")
print("=" * 40)
