import sys
input = sys.stdin.readline

def solve():
    def fact(n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        return n * fact(n - 1)
    n = int(input().strip())
    print(fact(n))

if __name__ == "__main__":
    solve()