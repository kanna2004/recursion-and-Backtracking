import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    def rec(n, s = 0):
        if n == 0:
            return s
        rec(n - 1, s + n)
    rec(n)
if __name__ == "__main__":
    solve()