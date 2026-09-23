import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a) - (n - 1))

t = int(input())
for _ in range(t):
    solve()