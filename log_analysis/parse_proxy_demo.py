import re
import pandas as pd
from datetime import datetime

def parse_proxy_log(log_file):
    events = []
    pattern = r'(\d+\.\d+)\s+\d+\s+(\S+)\s+(\S+)/(\d+)\s+(\d+)\s+(\S+)\s+(\S+)\s+-\s+(\S+)/(\S+)\s+(\S+)'
    with open(log_file, "r") as f:
        for line in f:
            match = re.match(pattern, line)
            if match:
                events.append({
                    "timestamp": datetime.fromtimestamp(float(match.group(1))),
                    "client_ip": match.group(2),
                    "status_code": match.group(3),
                    "response_size": int(match.group(5)),
                    "method": match.group(6),
                    "url": match.group(7),
                })
    return pd.DataFrame(events)

if __name__ == "__main__":
    df = parse_proxy_log(r"C:\Users\Dell\Desktop\Python_For_CyberSecurity\log_analysis\logs\proxy.log")
    print(df)
