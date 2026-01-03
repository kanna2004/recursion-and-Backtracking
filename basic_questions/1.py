import sys
input = sys.stdin.readline

def solve():
    def rec(n):
        if n == 0:
            return
        print(n)
        rec(n - 1)
    n = int(input().strip())
    rec(n)

if __name__ == "__main__":
    solve()