import pandas as pd
from datetime import datetime

# Hàm đọc firewall log
def parse_firewall_log(log_file):
    events = []  # danh sách lưu từng dòng log
    
    with open(log_file, "r") as f:
        for line in f:
            # bỏ qua dòng bắt đầu bằng "#" hoặc dòng trống
            if line.startswith("#") or line.strip() == "":
                continue  

            # tách log thành các trường (fields)
            fields = line.split()

            # chỉ xử lý khi đúng 10 trường
            if len(fields) == 10:
                timestamp = datetime.strptime(fields[0] + " " + fields[1], "%Y-%m-%d %H:%M:%S")
                action = fields[2]
                protocol = fields[3]
                src_ip = fields[4]
                dst_ip = fields[5]
                src_port = int(fields[6])
                dst_port = int(fields[7])
                size = int(fields[8])
                tcpflags = fields[9] if fields[9] != "-" else None

                # lưu lại thành dict
                event = {
                    "timestamp": timestamp,
                    "action": action,
                    "protocol": protocol,
                    "src_ip": src_ip,
                    "dst_ip": dst_ip,
                    "src_port": src_port,
                    "dst_port": dst_port,
                    "size": size,
                    "tcpflags": tcpflags
                }

                # thêm vào list
                events.append(event)

    # chuyển thành DataFrame (bảng dữ liệu)
    return pd.DataFrame(events)

# Chạy trực tiếp
if __name__ == "__main__":
    df = parse_firewall_log(r"C:\Users\Dell\Desktop\Python_For_CyberSecurity\log_analysis\logs\firewall.log")
    print(df)
