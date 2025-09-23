def count_abc_substrings(s):
    """
    Đếm số lượng xâu con "ABC" trong xâu s
    """
    count = 0
    for i in range(len(s) - 2):
        if s[i:i+3] == "ABC":
            count += 1
    return count

def solve():
    # Đọc input
    n, q = map(int, input().split())
    s = list(input().strip())
    
    # Xử lý từng truy vấn
    for _ in range(q):
        x, c = input().split()
        x = int(x) - 1  # Chuyển về chỉ số 0-based
        
        # Thay đổi ký tự tại vị trí x
        s[x] = c
        
        # Đếm số xâu con "ABC"
        result = count_abc_substrings(''.join(s))
        print(result)

# Chạy chương trình
if __name__ == "__main__":
    solve()