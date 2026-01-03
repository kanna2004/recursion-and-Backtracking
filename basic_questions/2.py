import sys
input = sys.stdin.readline

def solve():
    def rec(n, temp = 1):
        if temp == n + 16:
            return
        print(temp)
        rec(n, temp + 1)
    n = int(input().strip())
    rec(n)
if __name__ == "__main__":
    solve()