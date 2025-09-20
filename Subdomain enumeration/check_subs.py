#!/usr/bin/env python3
import sys
import requests

if len(sys.argv) != 2:
    print("Usage: python3 check_subs_simple.py target.com")
    sys.exit(1)

target = sys.argv[1].strip()

with open("subdomains.txt") as f:
    for line in f:
        sub = line.strip()
        if not sub:
            continue
        url = f"http://{sub}.{target}"
        try:
            r = requests.get(url, timeout=5)
        except requests.RequestException:
            continue
        else:
            print(f"Valid: {url}  (status: {r.status_code})")
