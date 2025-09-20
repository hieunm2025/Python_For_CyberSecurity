#!/usr/bin/env python3
import sys
import requests

if len(sys.argv) != 3:
    print("Usage: python3 dir_enum.py target.com /path/to/wordlist.txt")
    sys.exit(1)

target = sys.argv[1].strip()
wordlist_path = sys.argv[2]

with open(wordlist_path, "r") as f:
    for line in f:
        d = line.strip()
        if not d:
            continue
        url = f"http://{target}/{d}.html"
        try:
            r = requests.get(url, timeout=5)
        except requests.RequestException:
            continue
        if r.status_code != 404:
            print(f"Valid: {url}  (status: {r.status_code})")
