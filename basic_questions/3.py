import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    def rec(start, n):
        if start == n + 1:
            return
        print(start)
        rec(start + 1, n)
    rec(1, n)

if __name__ == "__main__":
    solve()