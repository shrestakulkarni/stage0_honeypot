import re
from collections import Counter
import os

LOG_FILE = "./simulated_logs.txt"
DECOY_DIR = "./honeypot_files"

ip_counter = Counter()
user_counter = Counter()
pass_counter = Counter()

line_re = re.compile(r"SRC=([0-9.]+)\s+LOGIN_ATTEMPT user=([^\s]+)\s+pass=([^\s]+)")

if not os.path.exists(LOG_FILE):
    print(f"Log file {LOG_FILE} not found. Run simulate_attacks.py first.")
    exit(1)

with open(LOG_FILE, "r", encoding="utf-8") as f:
    for line in f:
        m = line_re.search(line)
        if m:
            ip, user, pwd = m.group(1), m.group(2), m.group(3)
            ip_counter[ip] += 1
            user_counter[user] += 1
            pass_counter[pwd] += 1

print("=== Top attacker IPs ===")
for ip, c in ip_counter.most_common(10):
    print(f"{ip} — {c} attempts")

print("\n=== Top usernames tried ===")
for u, c in user_counter.most_common(10):
    print(f"{u} — {c} attempts")

print("\n=== Top passwords tried ===")
for p, c in pass_counter.most_common(10):
    print(f"{p} — {c} attempts")

# show decoy files
if os.path.isdir(DECOY_DIR):
    files = os.listdir(DECOY_DIR)
    print(f"\n=== Decoy files ({len(files)}) in {DECOY_DIR} ===")
    for fname in files[:20]:
        print("-", fname)
else:
    print(f"\nDecoy directory {DECOY_DIR} not found. Run make_decoys.py first.")
