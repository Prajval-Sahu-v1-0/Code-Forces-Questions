import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); a = int(data[idx+1]); b = int(data[idx+2])
        idx += 3
        if (n - b) % 2 != 0:
            out.append("NO")
        elif a <= b or (n - a) % 2 == 0:
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == "__main__":
    main()