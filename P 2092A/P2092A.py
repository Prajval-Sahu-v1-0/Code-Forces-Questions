import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = data[idx:idx+n]
        idx += n
        a = list(map(int, a))
        out.append(str(max(a) - min(a)))
    print("\n".join(out))

if __name__ == "__main__":
    main()