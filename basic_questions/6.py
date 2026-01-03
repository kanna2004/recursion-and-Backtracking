import sys
input = sys.stdin.readline

def solve():
    def N_Fib(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return N_Fib(n - 1)
    def tail_N_Fib(n, a = 0, b = 1):
        if n == 0:
            return a
        return tail_N_Fib(n - 1, b, a + b)
    n = int(input().strip())
    q = N_Fib(n)
    r = tail_N_Fib(n)
    print(q)
    print(r)
if __name__ == "__main__":
    solve()